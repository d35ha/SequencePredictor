A simple Sequence Predictor
# Examples
`Enter space separated list:1 2 3 4` Which is ruled by y=n as n is the index (1,2,3,..)<br/>
`Predicted value of index 5 is 5.0`<br/>
<br/>
`Enter space separated list:5 7 9` Which is ruled by y=3+2n as n is the index (1,2,3,..)<br/>
`Predicted value of index 4 is 12.0`<br/>
<br/>
`Enter space separated list:51` Which is ruled by y=51<br/>
`Predicted value of index 2 is 51.0`<br/>
<br/>
`Enter space separated list:-2 -4` Which is ruled by y=-2n as n is the index (1,2,3,..)<br/>
`Predicted value of index 3 is -6.0`<br/>
<br/>
`Enter space separated list:2.9 2.8 2.7 2.6` Which is ruled by y=3-0.1n as n is the index (1,2,3,..)<br/>
`Predicted value of index 5 is 2.5`<br/>
<br/>
`Enter space separated list:1 -5 -15` Which is ruled by y=3-2n^2 as n is the index (1,2,3,..)<br/>
`Predicted value of index 4 is -29.0`<br/>
<br/>
And for specific index values you can insert it as point <index,value_of_index> <br/>
<br/>
`Enter space separated list:2,9 3,-2 4,-10` Which is ruled by y=((3/2)n^2)-((37n)/2)+40 as n is the index (1,2,3,..)<br/>
`Predicted value of index 5 is 12.0`<br/>
<br/>
And to get the value of a specific index insert it like point <index,?> <br/>
<br/>
`Enter space separated list:9 6 1 8,?` Which is ruled by y=10-n^2 as n is the index (1,2,3,..)<br/>
`Predicted value of index 8 is -54.0`<br/>
<br/>
<br/>
`Enter space separated list:3,-18 5,100 1,0 -4,80 8,?` Which is ruled by y=n^2-n^3 as n is the index (1,2,3,..)<br/>
`Predicted value of index 8 is -448.0`<br/>
<br/>
# Important
The number of supplied items should not be less than the power of the predicted polynomial rule + 1<br/>
Using the two systems with each other like `1 3,9 2,4` is not allowed<br/>
Inserting two values for the same index like `1,2 1,3 2,4` is not allowed<br/>
