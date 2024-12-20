---
title: "HTB University CTF 2024"
summary: ""
categories: ["Writeups","Posts",]
tags: ["example", "tag"]
description: "a description"
date: 2024-12-20
draft: false
---

# HTB University CTF 2024 Writeups
Helloo. I recently participated in HTB’s University CTF 2024: Binary Badlands. Wanted to share some of my writeups for challenges I could solve. 🤡

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>

Category: `Coding`

Title: Frontier Cluster

Description:
Welcome back, Space Cowboy. The Minutemen have intercepted a cryptic signal from the Frontier Board—a corrupted data stream filled with duplicate entries. Hidden within this mess are critical coordinates that could lead us closer to the legendary Starry Spur.

Your mission is to sift through this chaotic stream and extract the unique entries. These coordinates must be preserved in the order they were received to maintain their integrity. Any duplicates are remnants of the Board's sabotage—eliminate them swiftly.

Once you've completed the task, report the refined list to Lena Starling. Time is of the essence, Cowboy—the resistance is counting on you!

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


Example
Input
String Input: 7 3 7 9 1 3 5 9

Output
String Expected Output: 7 3 9 1 5

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


~~~python
n = input()

numbers = n.split()  # Split input into a list of strings
seen = set()  # Set to track seen numbers
unique_numbers = []  # List to store unique numbers in order

for num in numbers:
    if num not in seen:
        seen.add(num)
        unique_numbers.append(num)

#print answer
print(" ".join(unique_numbers))
~~~

{{< alert icon="redflag" cardColor="#53659A" iconColor="#1d3557" textColor="#f1faee" >}}

HTB{r3m0v1ng_dup5_15_s0_345y_1F_y0u_kn0w_h0w_t0_c0d3!_e43188ed3c8f8c4a1983f7b8ba67e2ed}

{{< /alert >}}


<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


Category: `Coding`

Title: ConflictCruncher

Description:

Welcome back, Space Cowboy. The Minutemen have uncovered multiple encrypted data streams from the Frontier Board. These streams contain critical intelligence, but their keys overlap in ways that cause conflicts.

Your mission is to merge these conflicting data streams into a single dictionary. When conflicts arise (identical keys), you must apply the Frontier Protocol: retain the value from the second dictionary and discard the conflicting value from the first.

Complete this task swiftly and accurately, Cowboy, and report the unified dictionary back to Lena Starling. The fate of the resistance may depend on it!

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


Example
Input
String Dict input: {'a': 1, 'b': 2, 'c': 3}, {'b': 4, 'd': 5}

Output
Merged Output: {'a': 1, 'b': 4, 'c': 3, 'd': 5}

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>

~~~python
def conflict_cruncher(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# User input
input1 = eval(input())
input2 = eval(input())

# Perform the merge
merged_output = conflict_cruncher(input1, input2)

# Output the result
print(merged_output)
~~~

{{< alert icon="redflag" cardColor="#53659A" iconColor="#1d3557" textColor="#f1faee" >}}
HTB{n0w_1m_0ff1c4lly_4_c0nfl1ct_crunch3r_y4y!_09613d0c4ef180bac1c2bef4d5675f0f}
{{< /alert >}}

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


Category: `Coding`

Title: Energy Matrix Activation

Description:
Greetings, Space Cowboy. The resistance has uncovered the ancient Starry Spur, but its power lies dormant. To activate the energy matrix, you must combine specific energy crystals to reach a precise energy level.

Your mission is to calculate the number of ways to combine these crystals to match the required energy level. Each crystal can be used an unlimited number of times, but the combinations must add up to the exact target energy.

Report the number of valid combinations to Lena Starling. The fate of the resistance rests in your calculations!

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


Example
Input
Example 1:
Energy Crystals: [1, 2, 3]
Target Energy: 4

Example 2:
Energy Crystals: [2, 5, 3, 6]
Target Energy: 10

Output
Example 1 Output: 4
Explanation: There are 4 distinct ways to combine the crystals to reach the target energy level of 4:

    1. 1 + 1 + 1 + 1
    2. 1 + 1 + 2
    3. 2 + 2
    4. 1 + 3
Example 2 Output: 5
Explanation: There are 5 distinct ways to combine the crystals to reach the target energy level of 10:

    1. 2 + 2 + 2 + 2 + 2
    2. 2 + 2 + 2 + 2 + 2 + 2 + 3
    3. 2 + 2 + 2 + 6
    3. 5 + 5
    3. 2 + 3 + 5
Each combination adds up to the target energy level of 10. As before, the order of the crystals does not matter.


<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


~~~python
energy_crystals = input()
target_energy = input()

# Convert the input strings to proper data types
# Use eval() to interpret the list input and int() to convert the target energy
energy_crystals = eval(energy_crystals)
target_energy = int(target_energy)

def count_combinations(crystals, target):
    # Initialize the DP array
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: one way to make target 0
    
    # Update DP array for each crystal
    for crystal in crystals:
        for j in range(crystal, target + 1):
            dp[j] += dp[j - crystal]
    
    return dp[target]

# Calculate and print the result
result = count_combinations(energy_crystals, target_energy)
print(result)
~~~

{{< alert icon="redflag" cardColor="#53659A" iconColor="#1d3557" textColor="#f1faee" >}}
HTB{3n34gy_m4tr1x_act1v4t3d_w3_4r3_s4v3d!_fab10bcba322f2279d276e9e9e1fa5a4}
{{< /alert >}}

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


Category: `Coding`

Title: WordWrangler

Description:
Welcome, Space Cowboy. The Frontier Archives have transmitted an ancient text encrypted with layers of forgotten languages. The resistance needs your help to decode the most frequently used word in this transmission.

Your mission is to count the frequency of each word in the given text, ignoring case and punctuation, and identify the single most common word. If there are multiple words with the same highest frequency, return any one of them.

Answer Format:
Return the most common word as a single string. Do not include its count in the output.

Report the result back to Lena Starling. The resistance is counting on your precision and speed!

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


Input:
"The quick brown fox jumps over the lazy dog. The dog barks at the fox!"

Output:
the

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


~~~python
from collections import Counter
import string

def most_frequent_word(text):
    # Normalize the text: convert to lowercase and remove punctuation
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    # Split the text into words
    words = text.split()
    # Count the occurrences of each word
    word_counts = Counter(words)
    # Find the most frequent word
    most_frequent = max(word_counts, key=word_counts.get)
    return most_frequent

input_text = input()S
output = most_frequent_word(input_text)
print(output)
~~~

{{< alert icon="redflag" cardColor="#53659A" iconColor="#1d3557" textColor="#f1faee" >}}
HTB{pfupp_wh0_m4d3_th353_345y_ch4ll3ng35_ch1ld1sh!_94e2b14df5eebb43e53458c1ca33dca2}
{{< /alert >}}

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


Category: `Coding`

Title: Weighted Starfield Stabilizer

Description:
Welcome, Space Cowboy. The resistance has intercepted energy signals from the Frontier Starfield, but they are riddled with weighted anomalies that distort their stability. To analyze the starfield’s stability, you must calculate the maximum stability score.

Each energy signal is modified by its corresponding weight, creating a new stability signal:
Modified Signal = Signal × Weight

Your mission is to identify the maximum stability score for any contiguous subarray of the modified signals. Use your computational skills to ensure the accuracy of your findings!

Answer Format:
Return a single integer representing the maximum stability score from the starfield.

Report your findings to Lena Starling. The resistance depends on your precision to restore balance in the starfield!

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


Example
Input
Input:
signals = [1, -2, 3, -4]
weights = [2, 3, -1, 4]

Output
Output:
48
Explanation:
To compute the maximum stability score, follow these steps:

Calculate the modified signals:
- **[]()** 1 × 2 = 2
- **[]()** -2 × 3 = -6
- **[]()** 3 × -1 = -3
- **[]()** -4 × 4 = -16

The modified signals are:
- **[]()** [2, -6, -3, -16]

Find the maximum product of any contiguous subarray:


- **[]()** [2] : Product = 2
- **[]()** [-6] : Product = -6
- **[]()** [2, -6] : Product = -12
- **[]()** [-3, -16] : Product = 48

The maximum product is 48, which occurs for the subarray
- **[]()** [-3, -16]

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>

~~~python 
def maxStabilityScore(signals, weights):
    # Calculate the modified signals
    modified_signals = [signals[i] * weights[i] for i in range(len(signals))]

    # Initialize variables
    max_product = modified_signals[0]
    min_product = modified_signals[0]
    result = modified_signals[0]

    # Iterate over the modified signals
    for i in range(1, len(modified_signals)):
        if modified_signals[i] < 0:
            # If the current signal is negative, swap max_product and min_product
            max_product, min_product = min_product, max_product
        
        # Update the max and min product at the current index
        max_product = max(modified_signals[i], max_product * modified_signals[i])
        min_product = min(modified_signals[i], min_product * modified_signals[i])

        # Update the result to track the maximum product found
        result = max(result, max_product)

    return result

signals = eval(input())
weights = eval(input())
print(maxStabilityScore(signals, weights))  # Output: 48
~~~

{{< alert icon="redflag" cardColor="#53659A" iconColor="#1d3557" textColor="#f1faee" >}}
HTB{m1ssi0n_c0mpl3t3d_m4x1mum_5t4b1l1ty_4ch13v3d!_c3daa74241b0c220321f7f2371e79887}

{{< /alert >}}

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


Category: `Reversing`

Title: CryoWarmup

Description:
You've been on ice for a long time, so before you start your journey you'll need to defrost and warm up your skills. As luck would have it, you've forgotten the password to your trusty Electro-Safe-o-Matic, where your most prized possessions are. Can you still remember how to crack in?

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


You’re given a binary file. Run the following command to determine the type of a file:

```linux
file warmup
```
![](file.png#center)

since it’s not stripped, we can find the function names when we do dynamic analysis. 

Running the binary, it seems like a classic password checker program.
Giving the correct password will grant you access. So I went to Ghidra/Cutter to look at the source code.
![](chal.png#center)


There are 3 functions: main, validate_password, and generate_key. The generate_key function takes an input, performs XOR with 0x2a (42 in Decimal) for every bit, and adds 5 to it. 

1. What libc function is used to check if the password is correct?

![](strcmp.png#center)
strcmp

2. What is the size of the password buffer, based on the argument to scanf?

![](sizepassbuf.png#center)

49

3. What is the name of the function that modifies the user's input?

![](genkey.png#center)

generate_key

4. What would be the result of applying the operation from this function to a string containing one character, 'B'? Provide your answer as a hex number, e.g. 0x4f.

0x6f 'm'

5. What is printed if the password is correct?

"Access granted!"

6. How long is the password, based on the value that the user's input is compared against (not including the final null byte)?

8

7. What is the password?

Retrieve the original password by reversing the transformation process

Here’s the Python script to do so:

~~~python
def reverse_generate_key(target_hex):
    target_bytes = target_hex.to_bytes(8, byteorder="big")
    original_string = ""
    
    for byte in target_bytes:
        # Reverse (char ^ 0x2A) + 5
        original_char = (byte - 5) ^ 0x2A
        original_string += chr(original_char)
    
    # Reverse the final string
    return original_string[::-1]

target_hex = 0x625f491e53532047
original_string = reverse_generate_key(target_hex)
print(f"Reversed original string: {original_string}")
~~~

h1dd3npw

<div style="border-top: 2px solid #ccc; margin: 20px 0;"></div>


{{< alert icon="crown" cardColor="#53659A" iconColor="#1d3557" textColor="#f1faee" >}}
ada lagi writeups malas ah
{{< /alert >}}

