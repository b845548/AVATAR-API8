#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<string>
#include<string.h>




enum{
    STATE_INIT,
    STATE_START,
    STATE_MAKING,
    STATE_STARTSPEAK,
    STATE_SPEAKING,
};




class AliceScript{
	int state;
	std::string mBotName;	
	std::string mAnswer;
  public:
    AliceScript(void);
    int get_state(void);

	std::string get_answer(void);
    void set_state(int);
    void gen_answer(std::string);
    void gen_speak();
    void finish_make(void);
    void finish_speak(void);
    void set_botName(std::string);

};

