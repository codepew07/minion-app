import streamlit as st
import time
st.title("Welcome to Gru's lair" )
answer = st.text_input("Minions, should we steal the moon?!! (yes/no): ")
if answer: # Only process logic once something is typed
  lowered = answer.lower()   
  if lowered == "yes":
   st.success("Good Minion! You shall stay alongside me for you have proved your loyalty and gullibility. Now, let's head to the lab and commence the lunar theft protocol, through which I could set it off on nukes MUAHAHAHA.... *record scratch* wait I- er- didn't know- er- that you'd stick around hehe. I'd obviously 'not' do that. Infact, I would put a humongous leash around it and parade it through the neighbourhood haha. NOW ENOUGH DILLY-DALLYING, GET TO WORK BANANA HEADS!!!")
  elif lowered == "no":
        st.warning("Sigh...It's your loss that you're so boring.[You weren't invited to join us anyway.]")
  else:
        st.info("Well, aren't you quite the annoying one?") 
        time.sleep(2)
        with st.spinner("Here's a surprise for you...https://youtu.be/qxeokP0n6V0?si=Q6j1raRCwvQctLfz"):
         time.sleep(2)
         
       
       