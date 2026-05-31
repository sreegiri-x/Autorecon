from modules.scanner import run_scan

def main():
    target = input("Enter target IP: ")
    run_scan(target)

if __name__ == "__main__":
    main()