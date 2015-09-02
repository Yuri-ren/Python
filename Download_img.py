# -*- coding:utf-8 -*-
import re
import string 

def show_args_using_mutable_defaults(arg, def_arg=[]):
      def_arg.append("Hello World")
      return "arg={}, def_arg={}".format(arg, def_arg)
 
print show_args_using_mutable_defaults("test")
print show_args_using_mutable_defaults("test 2")
