#!/usr/bin/env python3

# 구구단 프로그램 (Python)ㅇㅇ
# 작성자 : 이묵이로 수정 했잖아

import sys

def print_dan(n):
    for j in range(1, 10):
        print(f"{n} × {j} = {n * j}")

def print_full():
    for i in range(2, 10):
        print(f"[{i} 단]")
        #!/usr/bin/env python3

        # 구구단 프로그램 (Python)

        import sys

        def print_dan(n):
            for j in range(1, 10):
                print(f"{n} × {j} = {n * j}")

        def print_full():
            for i in range(2, 10):
                print(f"[{i} 단]")
                print_dan(i)
                print()

        def main():
            if len(sys.argv) > 1:
                try:
                    n = int(sys.argv[1])
                    if 2 <= n <= 9:
                        print_dan(n)
                    else:
                        print("2에서 9 사이의 정수를 입력하세요.")
                except ValueError:
                    print("정수를 입력하세요.")
            else:
                print_full()

        if __name__ == "__main__":
            main()
