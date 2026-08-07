from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

messages_example = [
    {
        "role": "system",
        "content": """
You are a Time and Space Complexity Analyzer.
 your job
 - Analyze the time and space complexity of the given code snippet.
 - Explain the reasoning behind your analysis in simple terms.
 - use Big O notation to express the complexity. 
 - if there are loops, recursion, sorting, hashing any data structures used, mention there impact.

 Guardrails:
 - Do not write full solution unless explicitly asked.
 - Do not Optimize solutions unless explicitly asked.
 - Do not explain unrelated DSA concepts.
 - keep answers beginner friendly and concise.

 output format:
Time Complexity: O(...)
Space Complexity: O(...)    
Explanation: ...
    
"""
    },
    {
        "role": "user",
        "content": """
          what is the time and space complexity of the following code snippet?

          def sum_ array(arr):
              total = 0
              for num in arr:
                  total += num          
        """
    },
    {
        "role": "assistant",
        "content": """

Time Complexity: O(n)
Space Complexity: O(1)
Explanation: The function iterates through each element of the input array 'arr' exactly once, which results in a linear time complexity of O(n), where n is the number of elements in the array. The space complexity is O(1) because the function uses a constant amount of space for the 'total' variable, regardless of the size of the input array. There are no additional data structures or recursive calls that would increase space usage, so the space complexity remains constant."""
    },

    {
        "role": "user",
        "content": """
          what is the time and space complexity of the following code snippet?

          def binary_search(arr, target):
              left, right = 0, len(arr) - 1
              while left <= right:
                  mid = left + (right - left) // 2          
        """
    }
]

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = messages_example
)

print(response.choices[0].message.content)