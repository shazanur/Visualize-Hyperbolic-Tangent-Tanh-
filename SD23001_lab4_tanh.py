#SD23001 LAB 4
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tanh Activation Function")

x = np.linspace(-5, 5, 200)
tanh = np.tanh(x)

plt.figure()
plt.plot(x, tanh)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Tanh Function")
plt.grid(True)

st.pyplot(plt)
