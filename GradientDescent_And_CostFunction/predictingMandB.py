import numpy as np

def gradient_descent(x,y):

    m_curr = 0 #starting the initial value for m (coefficent as 0)
    b_curr = 0 #startting the initial value forb(intercept as 0)

    iterations = 1000 #number of iteration we want to iterate
    n = len(x)
    learning_rate = 0.08 #step size we want to decrese in each iteration

    for i in range(iterations):#

        y_predicted = m_curr*x+b_curr #from linear equation y = mx+b 
        # y = mx+b can be derived as y = y_predicted

        #cost_function determines how well are we doing 
        #  at each step we should be reducing the cost
        #The most nearly the cost value to zero the more accurate it is
        #If we find the optimim anwer the cost value donot change and remain same in each iteration
        cost = (1/n)*sum([val**2 for val in y-y_predicted])

        
        md = -(2/n)*sum(x*(y-y_predicted)) #partial derivation of Mean Square Error with respect to m(coefficent)
        bd = -(2/n)*sum(y-y_predicted) #partial derivation of Mean square Error with respect ot b(intercept)
        #md and bd gives direcion slope and direction

        #learning_rate is the stepsize we gradually reduce in each iteration to get into minima equation  
        m_curr = m_curr - learning_rate * md #the new result will be the m values getting closer to minima if done correctly
        b_curr = b_curr - learning_rate * bd #learning rate decreases the value of b nearly zero and multiplying it with bd(slope) gives you new value

        print("value of coefficent(m):{}, intercept(b):{}, Cost{}, iteration{}".format(m_curr,b_curr,cost,i))


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradient_descent(x,y)

#conclusion
# we used learning_rate = 0.08 and iteration 1000
#we got coefficient m = 2 and intercept(b) = 2.999999999, cost 1.51123123e-24(which is 0.24zero nearly zero)
#the predicted value is correct
#We knew Cost should reduce evry iteration
#We knew the more closer to zero the cost the accurate answer it is
# the learning rate should be examine with cost.