import unicodedata


# function that removes duplicated characters
def remove_duplicates(s):
  result = ''
  for i in range(len(s)):
    if i == 0 or s[i] != s[i - 1]:
      result += s[i]
  return result


# function that removes spaces
def remove_spaces(s):
  no_space = s.replace(" ", "")
  return no_space


# function that only keeps letters
def remove_all(s):
  all_removed = ''.join(c for c in s if c.isalpha())
  return all_removed


# function that only keeps letters and spaces
def remove_parts(s):
  parts_removed = ''.join(c for c in s if c.isalpha() or c.isspace())
  return parts_removed


# function that replaces special character with spaces
def replace_parts(s):
  parts_removed = ''.join(c if c.isalpha() or c.isspace() else ' ' for c in s)
  return parts_removed


# function that removes all non-latin characters
def remove_non_latin(s):
  return ''.join(c for c in s
                 if unicodedata.category(c) in ('Lu', 'Ll', 'Zs', 'Pc', 'Pd',
                                                'Ps', 'Pe', 'Pi', 'Pf', 'Po',
                                                'Nd', 'Sc'))


class SmartGuard:

  def __init__(self):
    self.last_messages_a1 = {}
    self.last_messages_a2 = {}
    self.last_messages_b1 = {}
    self.last_messages_b2 = {}
    self.last_messages_b3 = {}

  # removes all special characters, spaces so it is just pure plain text
  # first if tests with duplicates, second if without
  def check_a1(self, message, name, blacklist):
    if name not in self.last_messages_a1:
      self.last_messages_a1[name] = []

    message = remove_all(message.lower())
    self.last_messages_a1[name].append(message)

    if len(self.last_messages_a1[name]) > 20:
      self.last_messages_a1[name].pop(0)

    last_messages_str_a1 = ''.join(self.last_messages_a1[name])
    for word in blacklist:
      if word in last_messages_str_a1 or word in remove_duplicates(
          last_messages_str_a1):
        self.last_messages_a1[name] = []
        return True

  # removes all spaces but keep special characters
  # first if tests with duplicates, second if without
  def check_a2(self, message, name, blacklist):
    if name not in self.last_messages_a2:
      self.last_messages_a2[name] = []

    message = remove_spaces(message.lower())
    self.last_messages_a2[name].append(message)

    if len(self.last_messages_a2[name]) > 20:
      self.last_messages_a2[name].pop(0)

    last_messages_str_a2 = ''.join(self.last_messages_a2[name])
    for word in blacklist:
      if word in last_messages_str_a2 or word in remove_duplicates(
          last_messages_str_a2):
        self.last_messages_a2[name] = []
        return True

  # removes all special characters but keep spaces
  # a space is added at the end of each message in the table
  # first if tests with duplicates, second if without
  def check_b1(self, message, name, blacklist):
    if name not in self.last_messages_b1:
      self.last_messages_b1[name] = []

    message = (" " + remove_parts(message.lower()) + " ")
    self.last_messages_b1[name].append(message)

    if len(self.last_messages_b1[name]) > 20:
      self.last_messages_b1[name].pop(0)

    last_messages_str_b1 = ''.join(self.last_messages_b1[name])
    for word in blacklist:
      if word in last_messages_str_b1 or word in remove_duplicates(
          last_messages_str_b1):
        self.last_messages_b1[name] = []
        return True

  # replace all special characters with spaces
  # a space is added at the end of each message in the table
  # first if tests with duplicates, second if without
  def check_b2(self, message, name, blacklist):
    if name not in self.last_messages_b2:
      self.last_messages_b2[name] = []

    message = (" " + replace_parts(message.lower()) + " ")
    self.last_messages_b2[name].append(message)

    if len(self.last_messages_b2[name]) > 20:
      self.last_messages_b2[name].pop(0)

    last_messages_str_b2 = ''.join(self.last_messages_b2[name])
    for word in blacklist:
      if word in last_messages_str_b2 or word in remove_duplicates(
          last_messages_str_b2):
        self.last_messages_b2[name] = []
        return True

  # keep special characters and spaces but remove duplicates
  # a space is added at the end of each message in the table
  def check_b3(self, message, name, blacklist):
    if name not in self.last_messages_b3:
      self.last_messages_b3[name] = []

    message = (" " + remove_duplicates(message.lower()) + " ")
    self.last_messages_b3[name].append(message)

    if len(self.last_messages_b3[name]) > 20:
      self.last_messages_b3[name].pop(0)

    last_messages_str_b3 = ''.join(self.last_messages_b3[name])
    for word in blacklist:
      if word in last_messages_str_b3:
        self.last_messages_b3[name] = []
        return True

  # if a message has over 80% of capitalized letters, return true
  def check_caps(self, message):
    alpha = 0
    caps = 0
    for char in message:
      if char.isalpha():
        alpha += 1
      if char.isupper():
        caps += 1
    if caps > 0 and alpha > 0:
      result = caps / alpha
      if alpha > 8 and result > 0.8:
        return True

  # if a message has words longer than 20 char, return true
  def check_spam(self, s):
    s = remove_non_latin(s)
    words = s.split()
    for word in words:
      if len(word) > 20:
        return True

  # a master function to run all the checks
  def is_sus(self, content, author, blacklist_a, blacklist_b):
    if self.check_a1(
        content, author, blacklist_a) or self.check_a2(
            content, author, blacklist_a) or self.check_b1(
                content, author, blacklist_b) or self.check_b2(
                    content, author, blacklist_b) or self.check_b3(
                        content, author, blacklist_b) or self.check_caps(
                            content) or self.check_spam(content):
      return True
    else:
      return False
