"""Quick and simple demo for testing the code"""
from .ai import XrayScanner

scanner = XrayScanner()
prediction = scanner.scan_xray(image_path=input("Enter image path: "))
print("\n")
print(prediction)
