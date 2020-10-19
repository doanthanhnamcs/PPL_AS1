import unittest
from TestUtils import TestLexer    

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.checkLexeme("doan_thanh_nam123","doan_thanh_nam123,<EOF>",101))
	def test_102(self):
		self.assertTrue(TestLexer.checkLexeme("thanh nam","thanh,nam,<EOF>",102))
	def test_103(self):
		self.assertTrue(TestLexer.checkLexeme("thanhNam#","thanhNam,Error Token #",103))
	def test_104(self):
		self.assertTrue(TestLexer.checkLexeme("1813130nam","1813130,nam,<EOF>",104))
	def test_105(self):
		self.assertTrue(TestLexer.checkLexeme("1Nam","1,Error Token N",105))
	def test_106(self):
		self.assertTrue(TestLexer.checkLexeme("_nam123","Error Token _",106))
	def test_107(self):
		self.assertTrue(TestLexer.checkLexeme("1813130Tnam1813130","1813130,Error Token T",107))
	def test_108(self):
		self.assertTrue(TestLexer.checkLexeme("tnam1_8_1_3_1_3_0","tnam1_8_1_3_1_3_0,<EOF>",108))
	def test_109(self):
		self.assertTrue(TestLexer.checkLexeme("0n","0,n,<EOF>",109))
	def test_110(self):
		self.assertTrue(TestLexer.checkLexeme("DoanThanhNam","Do,anThanhNam,<EOF>",110))
	def test_111(self):
		self.assertTrue(TestLexer.checkLexeme("1230X123","1230,Error Token X",111))
	def test_112(self):
		self.assertTrue(TestLexer.checkLexeme("0847732066","0,847732066,<EOF>",112))
	def test_113(self):
		self.assertTrue(TestLexer.checkLexeme("0x1CD","0x1CD,<EOF>",113))
	def test_114(self):
		self.assertTrue(TestLexer.checkLexeme("0X123X123","0X123,Error Token X",114))
	def test_115(self):
		self.assertTrue(TestLexer.checkLexeme("0x123 0o123","0x123,0o123,<EOF>",115))
	def test_116(self):
		self.assertTrue(TestLexer.checkLexeme("0xABCDE 123","0xABCDE,123,<EOF>",116))
	def test_117(self):
		self.assertTrue(TestLexer.checkLexeme("0O7 0O8","0O7,0,Error Token O",117))
	def test_118(self):
		self.assertTrue(TestLexer.checkLexeme("12.","12.,<EOF>",118))
	def test_119(self):
		self.assertTrue(TestLexer.checkLexeme("0.25e3","0.25e3,<EOF>",119))
	def test_120(self):
		self.assertTrue(TestLexer.checkLexeme("12..56","12.,.,56,<EOF>",120))
	def test_121(self):
		self.assertTrue(TestLexer.checkLexeme("12e.03","12,e,.,0,3,<EOF>",121))
	def test_122(self):
		self.assertTrue(TestLexer.checkLexeme("0.e-123","0.e-123,<EOF>",122))
	def test_123(self):
		self.assertTrue(TestLexer.checkLexeme("1e-1.123","1e-1,.,123,<EOF>",123))
	def test_124(self):
		self.assertTrue(TestLexer.checkLexeme("12.04e-1","12.04e-1,<EOF>",124))
	def test_125(self):
		self.assertTrue(TestLexer.checkLexeme("True","True,<EOF>",125))
	def test_126(self):
		self.assertTrue(TestLexer.checkLexeme("Trueok","True,ok,<EOF>",126))
	def test_127(self):
		self.assertTrue(TestLexer.checkLexeme("TrueOk","True,Error Token O",127))
	def test_128(self):
		self.assertTrue(TestLexer.checkLexeme("Falseabc_","False,abc_,<EOF>",128))
	def test_129(self):
		self.assertTrue(TestLexer.checkLexeme("TrueFalsefalsetrue","True,False,falsetrue,<EOF>",129))
	def test_130(self):
		self.assertTrue(TestLexer.checkLexeme("Break" , "Break,<EOF>", 130))
	def test_131(self):
		self.assertTrue(TestLexer.checkLexeme("While" , "While,<EOF>", 131))
	def test_132(self):
		self.assertTrue(TestLexer.checkLexeme("WhileDoWhileBreakContinueForEndFor" , "While,Do,While,Break,Continue,For,EndFor,<EOF>", 132))
	def test_133(self):
		self.assertTrue(TestLexer.checkLexeme("Whileis_key_word_but_while_is_not_keyword" , "While,is_key_word_but_while_is_not_keyword,<EOF>", 133))
	def test_134(self):
		self.assertTrue(TestLexer.checkLexeme("IfFunctionParameterIF" , "If,Function,Parameter,Error Token I", 134))
	def test_135(self):
		self.assertTrue(TestLexer.checkLexeme("WhileDoingEndDo" , "While,Do,ingEndDo,<EOF>", 135))
	def test_136(self):
		self.assertTrue(TestLexer.checkLexeme("+-*\\" , "+,-,*,\\,<EOF>", 136))
	def test_137(self):
		self.assertTrue(TestLexer.checkLexeme("=====/=!=" , "==,==,=/=,!=,<EOF>", 137))
	def test_138(self):
		self.assertTrue(TestLexer.checkLexeme("======/=!=" , "==,==,==,Error Token /", 138))
	def test_139(self):
		self.assertTrue(TestLexer.checkLexeme("=====/=!==" , "==,==,=/=,!=,=,<EOF>", 139))
	def test_140(self):
		self.assertTrue(TestLexer.checkLexeme("+.-.*.\\." , "+.,-.,*.,\.,<EOF>", 140))
	def test_141(self):
		self.assertTrue(TestLexer.checkLexeme(">.<.==<=<=.>=>=.=" , ">.,<.,==,<=,<=.,>=,>=.,=,<EOF>", 141))
	def test_142(self):
		self.assertTrue(TestLexer.checkLexeme("{1.05,1,\"huhihihu\"}" , "{1.05,1,\"huhihihu\"},<EOF>", 142))
	def test_143(self):
		self.assertTrue(TestLexer.checkLexeme("{1,   3,5    }" , "{1,   3,5    },<EOF>", 143))
	def test_144(self):
		self.assertTrue(TestLexer.checkLexeme("{{    },{            } }" , "{{    },{            } },<EOF>", 144))
	def test_145(self):
		self.assertTrue(TestLexer.checkLexeme("{ {1,2,3},{4,5,6}}" , "{ {1,2,3},{4,5,6}},<EOF>", 145))
	def test_146(self):
		self.assertTrue(TestLexer.checkLexeme("{\"abc\",\"xyz\"}" , "{\"abc\",\"xyz\"},<EOF>", 146))
	def test_147(self):
		self.assertTrue(TestLexer.checkLexeme("{True,False,False,True}" , "{True,False,False,True},<EOF>", 147))
	def test_148(self):
		self.assertTrue(TestLexer.checkLexeme("{{1,2,3},{4,5,6,{7,8,9}}}" , "{{1,2,3},{4,5,6,{7,8,9}}},<EOF>", 148))
	def test_149(self):
		self.assertTrue(TestLexer.checkLexeme("{{1,2,3},{4,5,6,{7,8,9},   {10,11,12}}}" , "{{1,2,3},{4,5,6,{7,8,9},   {10,11,12}}},<EOF>", 149))
	def test_150(self):
		self.assertTrue(TestLexer.checkLexeme("{0xABC,2,0O320}" , "{0xABC,2,0O320},<EOF>", 150))
	def test_151(self):
		self.assertTrue(TestLexer.checkLexeme("{12e4,4.,0.}" , "{12e4,4.,0.},<EOF>", 151))
	def test_152(self):
		self.assertTrue(TestLexer.checkLexeme("{1,2 **haha**   }" , "{,1,,,2,},<EOF>", 152))
	def test_153(self):
		self.assertTrue(TestLexer.checkLexeme("\"Toi la Thanh Na123m\"","Toi la Thanh Na123m,<EOF>",153))
	def test_154(self):
		self.assertTrue(TestLexer.checkLexeme("\"Toi\tla Thanh Nam\"","Toi\tla Thanh Nam,<EOF>",154))
	def test_155(self):
		self.assertTrue(TestLexer.checkLexeme("\"Toi \t la \\f T Nam\"","Toi \t la \\f T Nam,<EOF>",155))
	def test_156(self):
		self.assertTrue(TestLexer.checkLexeme("\"Toi\\f \\b la Thanh Nam\"","Toi\\f \\b la Thanh Nam,<EOF>",156))
	def test_157(self):
		self.assertTrue(TestLexer.checkLexeme("\"New line string\\n is\"","New line string\\n is,<EOF>",157))
	def test_158(self):
		self.assertTrue(TestLexer.checkLexeme("\"string with special symbol \\n is\"","string with special symbol \\n is,<EOF>",158))
	def test_159(self):
		self.assertTrue(TestLexer.checkLexeme("\"Illegal esc ' ok \"","Illegal Escape In String: Illegal esc '",159))
	def test_160(self):
		self.assertTrue(TestLexer.checkLexeme("\"Illegal with more esc \\t \\k\"","Illegal Escape In String: Illegal with more esc \\t \\k",160))
	def test_161(self):
		self.assertTrue(TestLexer.checkLexeme("\"This is an unclose string \'\"","Unclosed String: This is an unclose string \'\"",161))
	def test_162(self):
		self.assertTrue(TestLexer.checkLexeme("\"He said: \'\"Thanh Nam dep trai \'\"\"","He said: \'\"Thanh Nam dep trai \'\",<EOF>",162))
	def test_163(self):
		self.assertTrue(TestLexer.checkLexeme("\"He said: \'\"Thanh Nam dep \\n trai \'\"\"","He said: \'\"Thanh Nam dep \\n trai \'\",<EOF>",163))
	def test_169(self):
		self.assertTrue(TestLexer.checkLexeme("\"He said: \'\"Thanh Nam dep \z trai \'\"\"","Illegal Escape In String: He said: \'\"Thanh Nam dep \z",169))
	def test_164(self):
		self.assertTrue(TestLexer.checkLexeme("**one\n*two\n*three\n**","<EOF>",164))
	def test_165(self):
		self.assertTrue(TestLexer.checkLexeme("**one\t \\k \b *#$#%@^^^**","<EOF>",165))
	def test_166(self):
		self.assertTrue(TestLexer.checkLexeme("**one\t \\k \b *#$#%@^^^*","Unterminated Comment",166))
	def test_167(self):
		self.assertTrue(TestLexer.checkLexeme("**one\t \\k \b **#$#%@^^^**","Error Token #",167))
	def test_168(self):
		self.assertTrue(TestLexer.checkLexeme("*****","*,<EOF>",168))
	def test_170(self):
		self.assertTrue(TestLexer.checkLexeme("Var: x=3,y=5,b=c,a,a,f={1,2};","Var,:,x,=,3,,,y,=,5,,,b,=,c,,,a,,,a,,,f,=,{1,2},;,<EOF>",170))
	def test_171(self):
		self.assertTrue(TestLexer.checkLexeme("var: a,b,c,d;","var,:,a,,,b,,,c,,,d,;,<EOF>",171))#var = id
	def test_172(self):
		self.assertTrue(TestLexer.checkLexeme("v=4+.3*.5-2=6.e4","v,=,4,+.,3,*.,5,-,2,=,6.e4,<EOF>",172))
	def test_173(self):
		self.assertTrue(TestLexer.checkLexeme("If(!a && b =/= c) Then z={1,5e99}","If,(,!,a,&&,b,=/=,c,),Then,z,=,{1,5e99},<EOF>",173))
	def test_174(self):
		self.assertTrue(TestLexer.checkLexeme("a[3+foo(i)] = b +. {1.2}","a,[,3,+,foo,(,i,),],=,b,+.,{1.2},<EOF>",174))
	def test_175(self):
		self.assertTrue(TestLexer.checkLexeme("a[0xAFF][3] != {{1,2,3},{4,5,6}}","a,[,0xAFF,],[,3,],!=,{{1,2,3},{4,5,6}},<EOF>",175))
	def test_176(self):
		self.assertTrue(TestLexer.checkLexeme("For(i=9;i<11;i=i+1)","For,(,i,=,9,;,i,<,11,;,i,=,i,+,1,),<EOF>",176))
	def test_177(self):
		self.assertTrue(TestLexer.checkLexeme("If \"string\" == True Then a = b","If,string,==,True,Then,a,=,b,<EOF>",177))
	def test_178(self):
		self.assertTrue(TestLexer.checkLexeme("If \"string\" ? True Then a = b","If,string,Error Token ?",178))
	def test_179(self):
		self.assertTrue(TestLexer.checkLexeme("If \"string\" != True Then a / b = 5;","If,string,!=,True,Then,a,Error Token /",179))
	def test_180(self):
		self.assertTrue(TestLexer.checkLexeme("If \"string\" != True Then a \\ b = 5;","If,string,!=,True,Then,a,\,b,=,5,;,<EOF>",180))
	def test_181(self):
		self.assertTrue(TestLexer.checkLexeme("If \"string \'\"abc\'\"\" != True Then a \\. b = 5;","If,string \"abc\",!=,True,Then,a,\.,b,=,5,;,<EOF>",181))
	def test_181(self):
		self.assertTrue(TestLexer.checkLexeme("If \"string\" != True **comment** Then a \\ b = 5;","If,string,!=,True,Then,a,\,b,=,5,;,<EOF>",181))
	def test_182(self):
		self.assertTrue(TestLexer.checkLexeme("If \"string\" != True **unclosecomment* Then a \\ b = 5;","If,string,!=,True,Unterminated Comment",182))
	def test_183(self):
		self.assertTrue(TestLexer.checkLexeme("**If \"string\" != True**  Then a \\ b = 5;","Then,a,\,b,=,5,;,<EOF>",183))
	def test_184(self):
		self.assertTrue(TestLexer.checkLexeme("If \"string\\' != True  Then a + b = 5;","If,Unclosed String: string\\' != True  Then a + b = 5;",184))
	def test_185(self):
		self.assertTrue(TestLexer.checkLexeme("\"Hello \\a \"","Illegal Escape In String: Hello \\a",185))
	def test_186(self):
		self.assertTrue(TestLexer.checkLexeme("\"Illegal with the \\' escape \'\" abcxyz \' \"","Illegal Escape In String: Illegal with the \\' escape \'\" abcxyz \'",186))
	def test_187(self):
		self.assertTrue(TestLexer.checkLexeme("\"A normal string nested string: \'\"a nested string\'\" \"","A normal string nested string: \'\"a nested string\'\" ,<EOF>",187))
	def test_188(self):
		self.assertTrue(TestLexer.checkLexeme("\"Some illegals '\" 'b \"","Illegal Escape In String: Some illegals \'\" '",188))
	def test_189(self):
		self.assertTrue(TestLexer.checkLexeme("\"Some illegals '\" \\nabc \\k \"","Illegal Escape In String: Some illegals \'\" \\nabc \k",189))
	def test_190(self):
		self.assertTrue(TestLexer.checkLexeme("\"Hello world**notcomment**","Unclosed String: Hello world**notcomment**",190))
	def test_191(self):
		self.assertTrue(TestLexer.checkLexeme("\"Hello world \\n '\"","Unclosed String: Hello world \\n \'\"",191))
	def test_192(self):
		self.assertTrue(TestLexer.checkLexeme("\"abc\",\"xyz\"","abc,,,xyz,<EOF>",192))
	def test_193(self):
		self.assertTrue(TestLexer.checkLexeme("\"abc\",\"xyz","abc,,,Unclosed String: xyz",193))
	def test_194(self):
		self.assertTrue(TestLexer.checkLexeme("not_errorChar,Error","not_errorChar,,,Error Token E",194))
	def test_195(self):
		self.assertTrue(TestLexer.checkLexeme("anErrorChar^","anErrorChar,Error Token ^",195))
	def test_196(self):
		self.assertTrue(TestLexer.checkLexeme("\"error char in string $##!@\"","error char in string $##!@,<EOF>",196))
	def test_197(self):
		self.assertTrue(TestLexer.checkLexeme("-3,-4,5,-0xFFFF,0","-,3,,,-,4,,,5,,,-,0xFFFF,,,0,<EOF>",197))
	def test_198(self):
		self.assertTrue(TestLexer.checkLexeme("\"abc\\\m\"","abc\\\m,<EOF>",198))
	def test_199(self):
		self.assertTrue(TestLexer.checkLexeme("**bbbjhgjh***","*,<EOF>",199))
	def test_100(self):
		self.assertTrue(TestLexer.checkLexeme("\"Minh \\\'la \\\ thanh\'\" \\\\nam\"","Minh \\\'la \\\ thanh\'\" \\\\nam,<EOF>",100))
		
        