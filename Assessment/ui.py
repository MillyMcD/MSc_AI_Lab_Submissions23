import tkinter as tk
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from sklearn import tree
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from database_client import DatabaseClient
from data_loader import DataLoader
from predictor import Predictor

#use this backend so we can draw matplotlib figures in our UI
matplotlib.use('TkAgg')

class PulsarUI:
    """
    The Pulsar Modelling UI. Enables you to log into your MongoDB database, before
    training a model and using it for inference
    """
    def __init__(self):
        #create a main window
        self.__mw = tk.Tk()

        #set a fixed geometry of 400 x 500 pixels
        self.__mw.geometry('400x500')

        #set a title
        self.__mw.title('Pulsar Prediction Tool')

        #create an empty list. We will dynamically store metric frames in here
        self.__metric_frames = []

        #placeholder for metrics
        self.__metrics = None

        #create the login window
        self.create_login_window()

        #run the main loop for rendering
        tk.mainloop()
    
    def create_login_window(self):
        """
        Create the Login window for the UI
        """
        #create the overall frame and a label providing instructions before packing
        login_frame = tk.Frame(self.__mw)
        top_label = tk.Label(login_frame,text='Please enter your Username and Password')
        top_label.pack()
        login_frame.pack()

        #create new frame to hold the username entry field
        lf1 = tk.Frame(login_frame)
        name_label = tk.Label(lf1,text='Username:')
        self.__name_entry = tk.Entry(lf1,width=10)
        name_label.pack(side='left')
        self.__name_entry.pack(side='left')
        lf1.pack()

        #create a new frame to hold the password entry field
        lf2 = tk.Frame(login_frame)
        pw_label = tk.Label(lf2,text='Password:')
        self.__pw_entry = tk.Entry(lf2,width=10,show="*")
        pw_label.pack(side='left')
        self.__pw_entry.pack(side='left')
        lf2.pack()

        #create a new frame to print message about login status
        lf3 = tk.Frame(login_frame)
        self.__login_res = tk.StringVar()
        login_label = tk.Label(login_frame,textvariable=self.__login_res)
        login_label.pack()
        lf3.pack()

        #create a new frame/button to attempt login
        lf4 = tk.Frame(login_frame)
        login_but = tk.Button(lf4,text='Login',width=10,command=self.login)
        login_but.pack()
        lf4.pack()

        #store the login frame as the current 'page' of the UI
        self.__this_page = login_frame

    def create_training_window(self):
        """"
        Create the training window for the UI. Allows you to train a decision tree using the data
        """

        #create a new frame, and a title for this page
        train_frame = tk.Frame(self.__mw)
        train_label = tk.Label(train_frame,text='Training Portal')
        train_label.pack()
        train_frame.pack()

        #create a frame and a new slider. This slider allows us to select what percentage
        #of the pulsar dataset will be used as the test set. By default 20% is used.
        tf1 = tk.Frame(train_frame)
        test_label  = tk.Label(tf1,text='Test Dataset size (%)')
        self.__test_slider = tk.Scale(tf1,from_=5,to=95,orient=tk.HORIZONTAL)
        self.__test_slider.set(20)  #default to 20%
        test_label.pack(side='left')
        self.__test_slider.pack(side='left')
        tf1.pack()
        
        #now create a frame/button to tell the UI to train the decision tree using the Predictor class.
        tf2 = tk.Frame(train_frame)
        train_but = tk.Button(tf2,text='Train Decision Tree',command=self.train)
        train_but.pack(pady=(20, 0)) #pad by 20 pixels to add some space
        tf2.pack()

        #We create six new frames ready for widgets to be added.
        #One for the 'metric' title, then one per classification metric,
        #which are accuracy, precision, recall and F1 score. Finally we have one for the 
        #decision tree drawing button.
        #this is done in this way so that we can have a navigation button at the bottom
        #it also allows us to rebuild the widgets each time the train button is pressed.
        self.__metric_frames = [tk.Frame(train_frame) for i in range(6)]
        for i in self.__metric_frames:
            i.pack()

        #finally we create a button to navigate to the inference window
        tf3 = tk.Frame(train_frame)
        to_infer = tk.Button(tf3,text='Go to Inference Portal',command=self.go_to_inference_window)
        to_infer.pack(pady=(50,0)) #pad by 50 pixels to add some space
        tf3.pack()

        #store the training window as the current 'page' of the UI
        self.__this_page = train_frame
    
    def create_inference_window(self):
        """
        Create the inference window for running the trained models
        """
        #follow same design as the training window
        infer_frame = tk.Frame(self.__mw)
        infer_label = tk.Label(infer_frame,text='Inference Portal')
        infer_label.pack()
        infer_frame.pack()

        #now add a label asking the user to add measurements
        if1 = tk.Frame(infer_frame)
        infer_title = tk.Label(if1,text='Please enter the fields below to classify your measurement')
        infer_title.pack(pady=(20,0))
        if1.pack()

        #Our dataset has 8 fields, which are given below
        fields = ['AvgObs', 'StdObs', 'KrtObs', 'SkwObs', 'AvgDMC',
                  'StdDMC', 'KrtDMC', 'SkwDMC']

        #create an dictionary where each value is None
        self.__infer_fields = {k:None for k in fields}
        
        #for loop through the fields, and create a frame, label and entry box
        #we set the dictionary to the entry box so we can get the values back later
        for field in fields:
            frame = tk.Frame(infer_frame)
            label = tk.Label(frame,text=field)
            entry = tk.Entry(frame,width=10)
            label.pack(side='left')
            entry.pack(side='left')
            frame.pack(side='top')
            self.__infer_fields[field] = entry

        #create a frame/button for calling inference via the Predictor class.
        if2 = tk.Frame(infer_frame)
        infer_button = tk.Button(if2,text='Infer Class',command = self.infer)
        infer_button.pack()
        if2.pack()

        #create a frame/label to provide messages such if the users' input is not complete
        #or if a model has not yet been trained appropriately.
        if3 = tk.Frame(infer_frame)
        self.__infer_res    = tk.StringVar()
        infer_rlab   = tk.Label(if3,textvariable=self.__infer_res)
        infer_rlab.pack(side='left',pady=(20,0))
        if3.pack()

        #as with the training window, create a button to navigate to the inference window
        if4 = tk.Frame(infer_frame)
        to_train = tk.Button(if4,text='Go to Training Portal',command=self.go_to_training_window)
        to_train.pack(pady=(30,0))
        if4.pack()

        #store the inference window as the current 'page' of the UI
        self.__this_page = infer_frame


    def login(self):
        """
        Login functionality, as used by the Login button on the main window
        """
        #grab username and password from the name/pw entry
        username = str(self.__name_entry.get())
        password = str(self.__pw_entry.get())

        #construct a client
        self.__client = DatabaseClient(
            username = username,
            password = password,
            dbname = 'pulsar_database')

        #check if we can log in. If not, update the login string on the UI to explain that creds
        #have failed.
        logged_in = self.__client.is_logged_in()
        login_str = 'Logged in! ' if logged_in else 'Login failed... Check your credentials'
        self.__login_res.set(login_str)

        #if successfully logged in, destroy this page and create the training window.
        if logged_in:
            self.__this_page.destroy()
            self.create_training_window()
    
    def train(self):
        """
        The training functionality, as used by the train button
        """
        #construct a dataloader using the client and 'raw_data' collection
        self.__dl = DataLoader(self.__client,'raw_data')

        #get the test size
        test_size = float(self.__test_slider.get()/100.)

        #build train/test sets
        X_train, X_test, y_train, y_test = self.__dl.prepare_data_training(test_size = test_size)

        #create a predictor/model and train it
        self.__predictor = Predictor()
        self.__predictor.train(X_train,y_train)
        print('Model Trained')

        #calculate metrics according to test set
        metrics = self.__predictor.report_performance(X_test,y_test)

        #sleep for 1 second
        time.sleep(1)

        #if our metric frames already have widgets, delete the widgets.
        #this is done everytime we press 'train'
        for i in self.__metric_frames:
            for widget in i.winfo_children():
                widget.destroy()

        #now construct the metrics and populate our metric frames.
        self.construct_metrics_and_tree(metrics)

    def construct_metrics_and_tree(self,metrics):
        """
        Contruct the test metrics and add a tree drawing button.

        Parameters
        ----------
        metrics : `dict`
            metrics dictionary 
        """
        #loop through the metrics (4 in total)
        for i,(key, value) in enumerate(metrics.items()):
            #grab the frame
            frame = self.__metric_frames[i]
            if i == 0:
                #if first frame, write a label and pack it
                metlabel = tk.Label(frame,text='Test set Metrics:')
                metlabel.pack(pady=(30,0))
            
            #else construct a label/and pack it.
            label  = tk.Label(frame,text=f'{key}: {value}')
            label.pack(side='left')
            #store metrics
            self.__metrics = metrics
        
        #now use the remaining frame to create a tree drawing button
        tree_but   = tk.Button(self.__metric_frames[-1],text='Draw Decision Tree',command=self.draw_tree)
        tree_but.pack()
        self.__metric_frames[-1].pack()
    
    def draw_tree(self):
        """"
        Draw the decision tree in a new window
        """
        #use tk's top level to create a pop-out window
        top = tk.Toplevel(self.__this_page)

        #build matplotlib figure/axis
        figure = plt.Figure((25,25))
        ax = figure.add_subplot(111)

        #grab tkagg canvas and plot the tree, grabbing the model from the predictor
        canvas = FigureCanvasTkAgg(figure, top)
        tree.plot_tree(self.__predictor.get_model(),ax=ax,fontsize=8)

        #create a toolbar. Doesn't seem to render properly?
        toolbar = NavigationToolbar2Tk(canvas, top)
        toolbar.update()

        #pack the canvas
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def infer(self):
        """
        Run inference using the trained model
        """
        infer_values = []
        #loop through the inference entry boxes and grab their values
        for key,value in self.__infer_fields.items():
            val = value.get()
            if len(value.get()) == 0:
                #if any value is empty, break the inference and update the message
                self.__infer_res.set('Provide a value for each measurement for inference')
                return
            #otherwise append
            infer_values.append(float(val))
        
        #convert to an array. Needs to be reshaped into 2d array else errors
        #this 'reshape' method is provided by the error
        test_data = np.array(infer_values).reshape(1,-1)

        #run inference only if the prediction object is available
        try:
            #use the dataloader to apply scaling used on training/test set
            test_data = self.__dl.prepare_data_inference(test_data)

            if self.__predictor.is_fitted():
                pred = self.__predictor.infer(test_data)

                #Pulsar if 1, else not pulsar
                pred_str = 'Pulsar' if pred[0]==1 else 'Not Pulsar'

                #update the message
                self.__infer_res.set(f'Sample predicted as: {pred_str}')
        except:
            #otherwise update message saying model hasn't been fitted
            self.__infer_res.set('Model is not fitted. Go to the Training Portal first')

    def go_to_inference_window(self):
        """
        Move to the inference window
        """
        self.__this_page.destroy()
        self.create_inference_window()
    
    def go_to_training_window(self):
        """
        Move to the training window
        """
        self.__this_page.destroy()
        self.create_training_window()

        #if we've calculated metrics previously but changed page
        #then redraw them back onto the page
        if self.__metrics is not None:
            self.construct_metrics_and_tree(self.__metrics)

ui = PulsarUI()
    