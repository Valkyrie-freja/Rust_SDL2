import os
import sys
import shutil
import subprocess

def main():
  # 実行された場所と同じディレクトリに Cargo.toml があるか確認
  if not os.path.exists('Cargo.toml'):
    print('Cargo.toml not found.')
    print('Please execute me at Cargo.toml.')
    #return
  
  # resource 内部をコピぺ
  exe_path = os.path.dirname(sys.argv[0])
  resoure_path = exe_path + '/resource'
  for copy_file in os.listdir(resoure_path):
    copy_file_path = f'{resoure_path}/{copy_file}'
    if os.path.isfile(copy_file_path) :
      shutil.copy( copy_file_path, copy_file)
    else:
      shutil.copytree( copy_file_path, copy_file)

  # .gitignore に/*.dll を加筆
  with open('.gitignore', mode='a') as gitignore:
    gitignore.write('/*.dll')
  
  # Cargo.toml の [package]以下に build = "build.rs" を追加
  with open('Cargo.toml', 'r+') as f:
    lines = f.readlines()
    package_next_index = lines.index('[package]\n') + 1
    lines.insert(package_next_index, 'build = "build.rs"\n')
    f.truncate(0)
    f.seek(0)
    f.writelines(lines)

  # cargo add sdl2 コマンドを実行
  subprocess.run(['cargo', 'add', 'sdl2'], shell=True)

main()