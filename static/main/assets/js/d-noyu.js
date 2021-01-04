// document.write('<link rel=stylesheet type="text/css" href="http://www.manythings.org/z/d.css">');
/*
Pull Down Menu Header -- Needed for Pages with Java and Random Sentences
*/
function menu(){
base = "http://www.manythings.org/";
site = "www.ManyThings.org";
pulldownmenu();
}
/*
Pull Down Menu
*/
function gu(form){
var ur=form.s.selectedIndex;
top.location.href=form.s.options[ur].value;
}
function pulldownmenu(){
base = "http://www.manythings.org/";
b = '<option value="'+base;
c = '</option>';
a='<center><form>';
//a+='<a href="javascript: history.go(-1)">&lt;&lt;</a> ';
// a+='<select name="s" onChange="gu(this.form)" size=1>';
// a+=b+'" selected="selected">Menu for '+site+c;
// a+=b+'">=== Main Menus ==='+c;
// a+=b+'">Home / Main Page</a>'+c;
// a+=b+'e/vocabulary.html">Menu: Vocabulary'+c;
// a+=b+'e/grammar.html">Menu: Grammar'+c;
// a+=b+'e/quiz.html">Menu: Grammar / Vocabulary Quizzes'+c;
// a+=b+'e/patterns.html">Menu: Patterns'+c;
// a+=b+'e/proverbs.html">Menu: Proverbs'+c;
// a+=b+'e/slang.html">Menu: Slang and Idioms'+c;
// a+=b+'e/pronunciation.html">Menu: Pronunciation'+c;
// a+=b+'e/listening.html">Menu: Listening'+c;
// a+=b+'e/hearing.html">Menu: Hearing'+c;
// a+=b+'e/podcasts.html">Menu: Podcasts / Songs / Jokes'+c;
// a+=b+'e/reading.html">Menu: Reading'+c;
// a+=b+'e/spelling.html">Menu: Spelling'+c;
// a+=b+'e/crosswords.html">Menu: Crossword Puzzles'+c;
// a+=b+'e/tt.html">Menu: Tongue Twisters and Poems'+c;
// a+=b+'e/voa.html">Menu: Voice of America (VOA) Materials'+c;
// a+=b+'e/misc.html">Menu: Misc. / Other Things'+c;
// a+=b+'e/crosswords.html">Menu: Crossword Puzzles'+c;
// a+=b+'e/tt.html">Menu: Tongue Twisters / Poems / Songs'+c;
// a+=b+'e/abc.html">Alphabetical List'+c;
a+='</select></form>';
a+='</center><p>';
document.write(a);
}


/* piwiki code 
var pkBaseURL = (("https:" == document.location.protocol) ? "https://www.manythings.org/piwikstats/" : "http://www.manythings.org/piwikstats/");
document.write(unescape("%3Cscript src='" + pkBaseURL + "piwik.js' type='text/javascript'%3E%3C/script%3E"));


try {
var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 1);
piwikTracker.trackPageView();
piwikTracker.enableLinkTracking();
} catch( err ) {}
*/
