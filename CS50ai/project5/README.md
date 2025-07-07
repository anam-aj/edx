1st:
    Convul-filter = 32
    convul-activation-function = relu
    hidden-units = 64
    hidden-activation-function = relu
    dropout = 0.25
    output-activation-function = softmax
    RESULT: 333/333 - 1s - 4ms/step - accuracy: 0.0556 - loss: 3.5057

2nd:
    Convul-filter = 32
    convul-activation-function = relu
    hidden-units = 64
    hidden-activation-function = relu
    dropout = 0.50
    output-activation-function = softmax
    RESULT: 333/333 - 1s - 4ms/step - accuracy: 0.0073 - loss: nan
3rd:
    Convul-filter = 32
    convul-activation-function = relu
    hidden-units = 64
    hidden-activation-function = softmax
    dropout = 0.25
    output-activation-function = softmax
    RESULT: 333/333 - 1s - 4ms/step - accuracy: 0.0525 - loss: 3.5019
