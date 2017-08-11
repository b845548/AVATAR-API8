#include"AliceScript.h"

AliceScript::AliceScript(void){
    state=STATE_INIT;    
    mBotName="skynet";
    system("rm test.wav");   
//    system("rm result.tmp");   
    system("rm finish.tmp");   
    system("rm question.tmp");   

}

void AliceScript::set_botName(std::string name){
    mBotName=name;
}

std::string AliceScript::get_answer(void){
    return mAnswer;
}

int AliceScript::get_state(void){
    return state;
}

void AliceScript::set_state(int state){
    this->state=state;
}

void AliceScript::gen_answer(std::string question){
    set_state(STATE_MAKING);
    FILE* f;
    f=fopen("question.tmp","w");
    fputs((question+"\nq").c_str(),f);
    fclose(f);
    std::string script = std::string("((java -cp out/production/Ab Main bot="+mBotName+" action=chat trace=false < question.tmp ) | grep 'Robot' > result.tmp; exit ) & (sleep 3 ; kill -9 $(ps aux | grep 'java -cp' | awk '{print $2}')) &");
    system(script.c_str());   

}


void AliceScript::finish_make(void){
FILE* f;
int count;
f=fopen("result.tmp","r");

if(f==NULL)
    return;
for(count=0;fgetc(f)!=EOF;count++);
fclose(f);
if(count<14)
    return;

set_state(STATE_STARTSPEAK);

}

void AliceScript::gen_speak(void){
FILE* f;
char * buff;
f=fopen("result.tmp","r");
if(f==NULL)
    return;
buff = (char *)malloc(1000*sizeof(char));
if(fgets(buff,1000,f)==NULL)
{
    free(buff);
    return;
}
std::string parse = std::string (buff); 
std::string answer = parse.substr (14,parse.size()-14);
mAnswer=answer;
std::string prefix = std::string("((pico2wave -l fr-FR -w test.wav \"");
std::string suffix = std::string("\"; aplay test.wav ; echo a > finish.tmp ); exit) &");

system((prefix+answer+suffix).c_str());
system("rm question.tmp");
system("rm result.tmp");
set_state(STATE_SPEAKING);
free(buff);
}

void AliceScript::finish_speak(void){
FILE* f;
f=fopen("finish.tmp","r");
if(f==NULL)
    return;
system("rm finish.tmp");
set_state(STATE_INIT);

}
/*
int main(){
AliceScript as;
std::string question=std::string("hello");
int stop=2;
while(stop){
std::cout<<as.get_state();
switch(as.get_state()){
    case STATE_INIT:
        stop--;
        as.gen_answer(question);
    break;
    case STATE_MAKING:
        as.finish_make();
    break;
    case STATE_STARTSPEAK:
        as.gen_speak();
    break;
    case STATE_SPEAKING:
        as.finish_speak();
    break;
    default:
    break;
    
}

}
}
*/
