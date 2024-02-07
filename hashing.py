#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

import hashlib
import uuid

# Function to generate a random salt using UUID
def salt:()
    return str(uuid.uuid4())

# Function to hash the password using PBKDF2-HMAC-SHA256
def hash_password( password, salt, iterations = 100000):

    # Using hashlib's pbkdf2_hmac with SHA256 as the hashing algorithm
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), iterations)
    return hashed_password

# Function to verify a password by comparing hashed input with stored hash
def verify(stored_hash, input_password, salt, iterations=100000):

    # Hash the input password using the same parameters as during hashing
    input_hash = hash_password(input_password, salt, iterations)

    # Check if the hashed input matches the stored hash
    return input_hash == stored_hash

# Example useage
user_password = "thisismysecurepassword123"
# Generate a random salt
user_salt = salt()
# Hash the users password
user_hashed_password = hash_password(user_password, user_salt)

# Verify the password by comparing the entered password with the stored hash
is_password_valid = verify(user_hashed_password, user_password, user_salt)
print("Is the password valid?", is_password_valid)
