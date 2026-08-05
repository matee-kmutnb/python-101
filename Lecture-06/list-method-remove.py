# Remove method
fruits_with_duplicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"Fruits after remove: {fruits_with_duplicates}")
# Output: Fruits after remove: ['banana', 'cherry', 'kiwi']
# ลบยังไงให้เหลือแค่ต้นฉบับ...