from flask import Flask, render_template, request, jsonify
from math import sqrt
import requests
import hashlib
import os

#Api funtions
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
