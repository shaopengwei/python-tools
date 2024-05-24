import os
 
def rename_files_in_folder(folder_path):
    """
    在指定文件夹中遍历文件，修改文件名。
    :param folder_path: 文件夹路径
    """
    for filename in os.listdir(folder_path):
        if '【' in filename:
            new_filename = filename.split("【")[0] + "." + filename.split(".")[1]
            old_filepath =  os.path.join(folder_path, filename)
            new_fliepath = os.path.join(folder_path, new_filename)
            os.rename(old_filepath, new_fliepath)

def change_file_attribute(folder_path):
    """
    修改文件属性信息
    """
    for filename in os.listdir(folder_path):
        file_stat = os.stat(os.path.join(folder_path, filename))

if __name__ == "__main__":
    # 使用示例
    change_file_attribute("D:\\音乐")