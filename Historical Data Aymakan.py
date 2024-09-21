import streamlit as st

# Title of the app
st.title("A Short Story")

# Subtitle or header
st.header("The Mysterious Forest")

# The story
story = """
Once upon a time, deep in a dense and mysterious forest, there was a young girl named Lily. 
Lily loved exploring the woods, even though the villagers often warned her about its secrets. 
One day, as she ventured deeper than ever before, she came across an ancient oak tree. 
The tree was unlike any she had seen before – its bark shimmered faintly, and its roots seemed to pulse with life.



In this hidden world, Lily discovered that the forest was alive and magical, protecting the land from unseen dangers. 
But the forest was weakening, and it needed a guardian. 
And so, Lily became the protector of the forest, ensuring that its magic would never fade away.

From that day forward, she was known as the Keeper of the Enchanted Wood, 
and the forest remained a place of wonder and mystery for all who dared to enter.
"""

# Display the story
st.write(story)

# Footer message
st.write("**The End**")
