Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Asus/Documents/Computer Vision/Assignments/Assignment4/Assignment4/Classifier.py
Using TensorFlow backend.
Train on 50000 samples, validate on 10000 samples
Epoch 1/5

Epoch 2/5

Epoch 3/5

Epoch 4/5

Epoch 5/5

Saved trained model at C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\saved_models\model_lr0.001.h5 
Test loss: 1.0117149381637573
Test accuracy: 0.6492999792098999
dict_keys(['val_loss', 'val_accuracy', 'loss', 'accuracy'])
>>> 
========= RESTART: C:/Users/Asus/Documents/Computer Vision/Assignments/Assignment4/Assignment4/Classifier.py ========
Using TensorFlow backend.
Train on 50000 samples, validate on 10000 samples
Epoch 1/5

Epoch 2/5

Epoch 3/5

Epoch 4/5

Epoch 5/5

Saved trained model at C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\saved_models\model_lr0.0001.h5 
Test loss: 1.4183944744110109
Test accuracy: 0.4909000098705292
dict_keys(['val_loss', 'val_accuracy', 'loss', 'accuracy'])

========= RESTART: C:/Users/Asus/Documents/Computer Vision/Assignments/Assignment4/Assignment4/Classifier.py ========
Using TensorFlow backend.
Train on 50000 samples, validate on 10000 samples
Epoch 1/5

Epoch 2/5

Epoch 3/5

Epoch 4/5

Epoch 5/5

Warning (from warnings module):
  File "C:\Program Files\Python37\lib\site-packages\keras\callbacks\callbacks.py", line 95
    % (hook_name, delta_t_median), RuntimeWarning)
RuntimeWarning: Method (on_train_batch_end) is slow compared to the batch update (1.109307). Check your callbacks.

Saved trained model at C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\saved_models\model_lr0.005.h5 
Test loss: 1.0451857349395752
Test accuracy: 0.6281999945640564
dict_keys(['val_loss', 'val_accuracy', 'loss', 'accuracy'])
>>> 
========= RESTART: C:/Users/Asus/Documents/Computer Vision/Assignments/Assignment4/Assignment4/Classifier.py ========
Using TensorFlow backend.
Train on 50000 samples, validate on 10000 samples
Epoch 1/5

Epoch 2/5

Epoch 3/5

Epoch 4/5

Epoch 5/5

Saved trained model at C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\saved_models\model_init_variance.h5 
Test loss: 1.0108812435150147
Test accuracy: 0.6434999704360962
dict_keys(['val_loss', 'val_accuracy', 'loss', 'accuracy'])
>>> 
========= RESTART: C:/Users/Asus/Documents/Computer Vision/Assignments/Assignment4/Assignment4/Classifier.py ========
Using TensorFlow backend.
Traceback (most recent call last):
  File "C:/Users/Asus/Documents/Computer Vision/Assignments/Assignment4/Assignment4/Classifier.py", line 69, in <module>
    opt=keras.optimizers.RMSprop(learning_rate=0.001, beta_1=0.9, beta_2=0.999, amsgrad=False)
  File "C:\Program Files\Python37\lib\site-packages\keras\optimizers.py", line 249, in __init__
    super(RMSprop, self).__init__(**kwargs)
  File "C:\Program Files\Python37\lib\site-packages\keras\optimizers.py", line 80, in __init__
    'passed to optimizer: ' + str(k))
TypeError: Unexpected keyword argument passed to optimizer: beta_1
>>> 
========= RESTART: C:/Users/Asus/Documents/Computer Vision/Assignments/Assignment4/Assignment4/Classifier.py ========
Using TensorFlow backend.
Train on 50000 samples, validate on 10000 samples
Epoch 1/5

Epoch 2/5

Epoch 3/5

Epoch 4/5

Epoch 5/5

Saved trained model at C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\saved_models\model_RMS.h5 
Test loss: 1.2412920251846313
Test accuracy: 0.5537999868392944
dict_keys(['val_loss', 'val_accuracy', 'loss', 'accuracy'])

========= RESTART: C:/Users/Asus/Documents/Computer Vision/Assignments/Assignment4/Assignment4/Classifier.py ========
Using TensorFlow backend.
Train on 50000 samples, validate on 10000 samples
Epoch 1/5

Epoch 2/5

Epoch 3/5

Epoch 4/5

Epoch 5/5

Saved trained model at C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\saved_models\model_dropout_0.1.h5 
Test loss: 0.9604701740264893
Test accuracy: 0.6632999777793884
dict_keys(['val_loss', 'val_accuracy', 'loss', 'accuracy'])

========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]]
Horse
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[1.9505833e-16 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00
  1.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00]]
Dog
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]]
Truck
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]]
Horse
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]]
Bird
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]]
Dog
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
Aeroplane
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
Aeroplane
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]]
Horse
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]]
Horse
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]]
Frog
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]]
Frog
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]]
Horse
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
Aeroplane
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]]
Ship
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]]
Dog
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0.0000000e+00 0.0000000e+00 0.0000000e+00 1.6269012e-34 0.0000000e+00
  1.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00]]
Dog
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0.0000000e+00 0.0000000e+00 0.0000000e+00 1.6269012e-34 0.0000000e+00
  1.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00]]
Dog
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
Aeroplane
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]]
Truck
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]]
Frog
>>> 
========== RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Predict.py ==========
Using TensorFlow backend.
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]]
Truck
>>> 
========= RESTART: C:\Users\Asus\Documents\Computer Vision\Assignments\Assignment4\Assignment4\Classifier.py ========
Using TensorFlow backend.
Train on 50000 samples, validate on 10000 samples
Epoch 1/50

Epoch 2/50

Epoch 3/50

Epoch 4/50

Epoch 5/50

Epoch 6/50

Epoch 7/50

Epoch 8/50

Epoch 9/50

Epoch 10/50

Epoch 11/50

Epoch 12/50

Epoch 13/50

Epoch 14/50

Epoch 15/50

Epoch 16/50

Epoch 17/50

Epoch 18/50

Epoch 19/50

Epoch 20/50

Epoch 21/50

Epoch 22/50

Epoch 23/50

Epoch 24/50

Epoch 25/50

Epoch 26/50

Epoch 27/50

Epoch 28/50

Epoch 29/50

Epoch 30/50
