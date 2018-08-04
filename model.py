import tflearn as tfl
import time #track time that is needed for training

class DFFP():
    """
    Deep-feed-forward-perceptron class
    """
    def __init__(self,checkpoint_path, model_path):
        self.checkpoint_path=checkpoint_path
        self.learning_rate=1e-5
        self.model_path=model_path

    def __init_model(self,load=False):
        """
        Init the model
        """
        net=tfl.layers.input_data(shape=[None,])
        net=tfl.layers.core.fully_connected(net,n_units=200,activation="relu")
        net=tfl.layers.core.fully_connected(net,n_units=350,activation="relu")
        net=tfl.layers.core.fully_connected(net,n_units=100,activation="relu")
        net=tlf.layers.core.fully_connected(net,n_units=50,activation="relu")
        net=tlf.layers.core.fully_connected(net,n_units=1,activation="sigmoid")
        net=tfl.layers.estimator.regression(net,learning_rate=self.learning_rate)
        model=tfl.models.DNN(net,checkpoint_path=self.checkpoint_path)
        if not load:
            return model
        if load:
            return model
        else:
            raise ValueError("Input has to be either True or False!")

    def train_on_batches(self,x,y):
        """
        Train model on batches
        Parameters:
            x: input data
            y: target data
        """
        model=self.__init_model()
        batch_n=0
        t=time.time()
        for a,b in zip(x,y):
            print("Fitting singele batch... {0} from {1}".format(batch_n,len(x)))
            model.fit_batch(a,b)
            batch_n+=1
        model.save(model_path)
        t2=time.time()
        print("Time needed: {} min. ".format((t2-t)/60))

    def train(self,x,y,n_e=10):
        """
        Train model
        Parameters:
            x: input data
            y: target data
        """
        model=self.__init_model()
        model.fit(x,y,validation_set=0.1,n_epoch=n_e)
        model.save(self.model_patH)

    def predict(self,x):
        """
        Predict new input
        Parameters:
            x: input data
        """
        model=self.__init_model(True)
        return model.predict(x)

    def evaluate(self,x,y):
        model=self.__init_model(True)
        model.evaluate(x,y)
