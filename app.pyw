import os, shutil, colorama
from obfuscator import Obfuscator

colorama.init()

def main():
  obfuscator = Obfuscator()
  files = obfuscator.getFiles()

  for folder in files['folder']:
    if not os.path.exists(folder):
      try:
        os.makedirs(folder)
        print('folder create', '[ \x1b[1;32mOK\x1b[0m ]', folder)
      except:
        print('folder create', '[ \x1b[1;31mFAIL\x1b[0m ]', folder)

    else:
      print('folder create', '[ \x1b[1;37mEXISTS\x1b[0m ]', folder)


  for file in files['file']:
    if ('.py' == os.path.splitext(file['source'])[1]):
      try:
        f = open(file['source'])
        compileFile = compile(f.read(), os.path.splitext(os.path.basename(file['source']))[0], 'exec')
        content = obfuscator.run(compileFile)

        nf = open(file['destination'], 'w')
        nf.write(content)
        nf.close()

        print('encode file', '[ \x1b[1;32mOK\x1b[0m ]', file['source'], '=>', file['destination'])

      except:
        print('encode file', '[ \x1b[1;31mFAIL\x1b[0m ]', file['source'], '=>', file['destination'])

    else:
      try:
        shutil.copy2(file['source'], file['destination'])
        print('copy file', '[ \x1b[1;32mOK\x1b[0m ]', file['source'], '=>', file['destination'])

      except:
        print('copy file', '[ \x1b[1;31mFAIL\x1b[0m ]', file['source'], '=>', file['destination'])

if __name__ == '__main__':
  main()