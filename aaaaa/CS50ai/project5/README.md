Experimented with everything, tried different combinations of activation model. Also increased number of filters upto 256 and same for number of nodes in hidden layer. But none of these had much effect on accuracy, it remained around 50%. However the training time had incresed significantly.

Finally when changed the dimension of filters to (6, 6) then it had drastic effect on accuracy, any above or below values for filter were affecting accuracy negatively. Also making the dropout equal to 0.25 also helped in accuracy increasing further, though not very significantly.

Still final accuracy achieved is only about 90% with keeping the training time low.
