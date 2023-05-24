import streamlit as st
from main import sex_deadh

def test_male():
    data = ["0,1,2,3,4,female", "1,1,2,3,4,male", "2,1,2,3,4,male", "3,1,2,3,4,male"]
    assert sex_deadh(data, "male") == 100

def test_female():
    data = ["0,1,2,3,4,male", "1,1,2,3,4,female", "2,1,2,3,4,male", "3,0,2,3,4,female"]
    assert sex_deadh(data, "female") == 50

def test_deadh_all_male():
    data = ["0,0,2,3,4,female", "1,0,2,3,4,male", "2,0,2,3,4,female", "1,0,2,3,4,male"]
    assert sex_deadh(data, "male") == 0

def test_deadh_all_female():
    data = ["0,0,2,3,4,female", "1,0,2,3,4,male", "2,0,2,3,4,female", "1,0,2,3,4,male"]
    assert sex_deadh(data, "female") == 0
