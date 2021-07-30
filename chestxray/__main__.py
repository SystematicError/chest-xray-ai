"""Quick and simple demo for testing the code"""
from .xray import XrayScanner

scanner = XrayScanner()
prediction = scanner.scan_xray(image_path=input("Enter image path: "))
print("\n")
print(prediction)
