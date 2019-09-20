from math import ceil, log
import marshal, os


class Obfuscator():
  settings: {}

  def __init__(self):
    self.settings = {
      'path': {
        'source': 'resources/source/',
        'destination': 'resources/destination/'
      },

      'content': {
        'header': "(lambda __, ___, ____, _____, ______, _______, ________, _________: getattr(" \
                  "__import__('\\x62\\x75\\x69\\x6c\\x74\\x69\\x6e\\x73')," \
                  " '\\x65\\x78\\x65\\x63')(getattr(__import__(" \
                  "'\\x6d\\x61\\x72\\x73\\x68\\x61\\x6c'), '\\x6c\\x6f\\x61\\x64\\x73')" \
                  "((lambda ______________, _______________: getattr(" \
                  "(lambda: 0).__code__.co_lnotab, '\\x6a\\x6f\\x69\\x6e')(" \
                  "[______________(______________, ________________)[__:__ - ___] " \
                  "for ________________ in _______________]))(lambda _________________," \
                  " __________________: getattr(__import__(" \
                  "'\\x62\\x75\\x69\\x6c\\x74\\x69\\x6e\\x73')," \
                  " '\\x62\\x79\\x74\\x65\\x73')([__________________ %" \
                  " (__ << _________)]) + _________________(_________________," \
                  " __________________ // (__ << _________)) if" \
                  " __________________ else (lambda: 0).__code__.co_lnotab, [",
        'footer': "])), getattr(__import__('\\x62\\x75\\x69\\x6c\\x74\\x69\\x6e\\x73')," \
                  " '\\x67\\x6c\\x6f\\x62\\x61\\x6c\\x73')()))(*(lambda _, __, ___:" \
                  " _(_, __, ___))((lambda _, __, ___: [__(___[(lambda: _).__code__.co_nlocals])" \
                  "] + _(_, __, ___[(lambda _: _).__code__.co_nlocals:]) if ___ else []), lambda" \
                  " _: _.__code__.co_argcount, (lambda _: _, lambda _, __: _, lambda _, __, ___:" \
                  " _, lambda _, __, ___, ____: _, lambda _, __, ___, ____, _____: _, lambda" \
                  " _, __, ___, ____, _____, ______: _, lambda _, __, ___, ____, _____, ______," \
                  " _______: _, lambda _, __, ___, ____, _____, ______, _______, ________: _)))"
      }
    }

  def run(self, source):
    codeBytes = marshal.dumps(source, 2)
    return ''.join([
      self.settings['content']['header'],
      ', '.join(self.convert(codeBytes)),
      self.settings['content']['footer']
    ])

  def convert(self, instring):
    blocks = self.getBlocks(instring)
    return [self.numConvert(block) for block in blocks]

  def encode(self, num, depth):
    if num == 0:
      return '__ - __'
    if num <= 8:
      return '_' * (num + 1)
    return '(' + self.numConvert(num, depth + 1) + ')'

  # Ben Kurtovic's bitshift conversion algorithm:
  # https://benkurtovic.com/2014/06/01/obfuscating-hello-world.html
  def numConvert(self, num, depth=0):
    result = ''
    while num:
      base = shift = 0
      diff = num
      span = int(ceil(log(-num if num < 0 else num, 1.5))) + (16 >> depth)
      for test_base in range(span):
        for test_shift in range(span):
          test_diff = (-num if num < 0 else num) - (test_base << test_shift)
          if (-test_diff if test_diff < 0 else test_diff) < (-diff if diff < 0 else diff):
            diff = test_diff
            base = test_base
            shift = test_shift

      if result:
        result += ' + ' if num > 0 else ' - '
      elif num < 0:
        base = -base

      if shift == 0:
        result += self.encode(base, depth)
      else:
        result += '(%s << %s)' % (self.encode(base, depth),
                                  self.encode(shift, depth))
      num = diff if num > 0 else -diff

    return result

  def getBlocks(self, message, block_size=16):
    block_nums = []

    for block in [message[i:i + block_size] for i in range(0, len(message), block_size)]:
      block = b'\x80' + block + b'\x80'
      block_num = 0
      block = block

      for i, char in enumerate(block):
        block_num += char * (256 ** i)

      block_nums.append(block_num)

    return block_nums

  def getFiles(self):
    files = {
      'folder': [],
      'file': []
    }

    # r=root, d=directories, f = files
    for r, d, f in os.walk(self.settings['path']['source']):
      for directory in d:
        files['folder'].append(os.path.join(self.settings['path']['destination'], directory))

      for file in f:
        sourceFile = os.path.join(r, file)
        sourceFileSubDirectory = os.path.dirname(sourceFile[len(self.settings['path']['source']):])
        destinationFile = os.path.join(os.path.join(self.settings['path']['destination'], sourceFileSubDirectory), file)

        files['file'].append({
          'source': sourceFile,
          'destination': destinationFile,
        })

    return files
