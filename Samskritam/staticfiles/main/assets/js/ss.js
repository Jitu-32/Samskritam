//Dennie Hoopingarner's http://clear.msu.edu/dennie/matic/mixer/

function init(){
    // Populate the Array
    myArray0=S0.split(" ")
    myArray1=S1.split(" ")
    myArray2=S2.split(" ")
    myArray3=S3.split(" ")
    myArray4=S4.split(" ")
    myArray5=S5.split(" ")
    myArray6=S6.split(" ")
    myArray7=S7.split(" ")
    myArray8=S8.split(" ")
    myArray9=S9.split(" ")
    // Do this for each sentence
    for(AC=0;AC<=9;AC++){popNewArray()}}
    
    // get random array elements
    // Gotta re-initialize the RA
    function popNewArray(){RA.length=0;for(var i=0;i<=(eval("myArray"+AC)).length;i++){genNum();RA[i]=R+(eval("myArray"+AC))[i]};writeThem()}
    
    // Generate a Random number
    function genNum(){R=parseInt(Math.random()*9+1)}
    
    // The buttons for the words.
    function writeThem(){RA.sort()
    document.writeln("<A HREF='javascript:myClear("+AC+")'>CLEAR</A>")
    document.writeln("<input type=TEXT size=50 name='MS" +AC+"')>")
    document.writeln(" <A HREF='javascript:checkIt("+AC+")'>CHECK</A>")
    document.writeln("<BR>")
    for(var i=0;i<(eval("myArray"+AC)).length;i++){
    document.writeln("<input type='button' value='"+RA[i].substr(1, RA[i].length)+"' onClick='Javascript:writeIt(this, "+AC+")'>")
    }
    document.writeln("</TD></TR></TABLE><P>")}
    
    function writeIt(myWord, SC){
    if(eval("document.forms[1].MS"+SC+".value")==""){eval("document.forms[1].MS"+SC+".value='"+myWord.value+" '")
    }else{eval("document.forms[1].MS"+SC+".value='"+eval("document.forms[1].MS"+SC+".value")+ myWord.value+" '")
    }}
    
    function myClear(SC){eval("document.forms[1].MS"+SC+".value=''")}
    
    function checkIt(SC){studentArray=new Array();correctArray=new Array();
    myWrong=0
    CA=(eval("S"+SC))
    studentAnswerA=eval("document.forms[1].MS"+SC+".value")
    studentAnswer=studentAnswerA.substr(0, studentAnswerA.length - 1)
    if(CA==studentAnswer){
    alert("Correct.")
    }else{
    correctArray=CA.split(" ")
    studentArray=studentAnswer.split(" ")
    // Check the studentAnswer, word by word
    myRight=correctArray.length
    for(var i=0;i<=correctArray.length;i ++){
    if(studentArray[i]!=correctArray[i]){
    myWrong ++
    }}
    alert("Out of a total of "+correctArray.length+" words, you got "+myWrong+" words wrong.")
    }}
    myArray0=new Array();
    myArray1=new Array();
    myArray2=new Array();
    myArray3=new Array();
    myArray4=new Array();
    myArray5=new Array();
    myArray6=new Array();
    myArray7=new Array();
    myArray8=new Array();
    myArray9=new Array();
    RA=new Array();
    R=0
    AC=0
    