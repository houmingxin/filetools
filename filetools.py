
def write_file(file_name, content):
    """
        写入文件
    """
    with open(file_name, "w") as f:
        f.write(content)

def read_file(file_path):
    result = ""
    with open(file_path, "r") as f:
        result = f.readline()

    return result


# if __name__ == "__main__":
#     # write_file("./user_token.txt", "123dqfqdqwfqwd")
#     token = read_file("./user_token.txt")
#     print(token)