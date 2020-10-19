# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0270\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\7\2\u009e\n\2\f\2\16\2\u00a1\13\2\3\3")
        buf.write("\3\3\3\3\7\3\u00a6\n\3\f\3\16\3\u00a9\13\3\3\3\3\3\5\3")
        buf.write("\u00ad\n\3\3\4\3\4\5\4\u00b1\n\4\3\5\6\5\u00b4\n\5\r\5")
        buf.write("\16\5\u00b5\3\5\5\5\u00b9\n\5\3\5\3\5\3\5\6\5\u00be\n")
        buf.write("\5\r\5\16\5\u00bf\3\5\3\5\5\5\u00c4\n\5\5\5\u00c6\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3<\3<\3=\3=\3=\3=\3=\3=\7=\u01a6\n=\f=\16=")
        buf.write("\u01a9\13=\3=\3=\3=\3=\3=\3>\3>\7>\u01b2\n>\f>\16>\u01b5")
        buf.write("\13>\3>\7>\u01b8\n>\f>\16>\u01bb\13>\3>\3>\3>\3>\3>\5")
        buf.write(">\u01c2\n>\3>\7>\u01c5\n>\f>\16>\u01c8\13>\3>\7>\u01cb")
        buf.write("\n>\f>\16>\u01ce\13>\3>\3>\7>\u01d2\n>\f>\16>\u01d5\13")
        buf.write(">\3>\3>\3>\3>\3>\5>\u01dc\n>\3>\7>\u01df\n>\f>\16>\u01e2")
        buf.write("\13>\7>\u01e4\n>\f>\16>\u01e7\13>\3>\7>\u01ea\n>\f>\16")
        buf.write(">\u01ed\13>\5>\u01ef\n>\3>\7>\u01f2\n>\f>\16>\u01f5\13")
        buf.write(">\3>\3>\3?\3?\3@\3@\3A\3A\6A\u01ff\nA\rA\16A\u0200\3A")
        buf.write("\6A\u0204\nA\rA\16A\u0205\3A\7A\u0209\nA\fA\16A\u020c")
        buf.write("\13A\3B\3B\6B\u0210\nB\rB\16B\u0211\3B\6B\u0215\nB\rB")
        buf.write("\16B\u0216\3B\7B\u021a\nB\fB\16B\u021d\13B\3C\3C\5C\u0221")
        buf.write("\nC\3C\6C\u0224\nC\rC\16C\u0225\3D\3D\7D\u022a\nD\fD\16")
        buf.write("D\u022d\13D\3E\6E\u0230\nE\rE\16E\u0231\3E\3E\3F\3F\3")
        buf.write("F\3F\5F\u023a\nF\3G\3G\3G\3H\3H\3H\5H\u0242\nH\3I\3I\7")
        buf.write("I\u0246\nI\fI\16I\u0249\13I\3I\3I\3I\3J\3J\7J\u0250\n")
        buf.write("J\fJ\16J\u0253\13J\3J\3J\3J\3K\3K\7K\u025a\nK\fK\16K\u025d")
        buf.write("\13K\3K\5K\u0260\nK\3K\3K\3L\3L\3L\3L\3L\7L\u0269\nL\f")
        buf.write("L\16L\u026c\13L\3M\3M\3M\2\2N\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62")
        buf.write("c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081\2\u0083")
        buf.write("\2\u0085\2\u0087\2\u0089B\u008b\2\u008d\2\u008f\2\u0091")
        buf.write("C\u0093D\u0095E\u0097F\u0099G\3\2\24\3\2c|\6\2\62;C\\")
        buf.write("aac|\3\2\62\62\3\2,,\3\2\62;\3\2\63;\4\2ZZzz\4\2\63;C")
        buf.write("H\4\2\62;CH\4\2QQqq\3\2\639\3\2\629\5\2GGgg~~\4\2--//")
        buf.write("\5\2\13\f\17\17\"\"\6\2\f\f$$))^^\t\2))^^ddhhppttvv\3")
        buf.write("\3\f\f\2\u0298\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u009b\3\2\2\2\5\u00ac")
        buf.write("\3\2\2\2\7\u00b0\3\2\2\2\t\u00c5\3\2\2\2\13\u00c7\3\2")
        buf.write("\2\2\r\u00cc\3\2\2\2\17\u00d2\3\2\2\2\21\u00db\3\2\2\2")
        buf.write("\23\u00de\3\2\2\2\25\u00e3\3\2\2\2\27\u00ea\3\2\2\2\31")
        buf.write("\u00f2\3\2\2\2\33\u00f8\3\2\2\2\35\u00ff\3\2\2\2\37\u0108")
        buf.write("\3\2\2\2!\u010c\3\2\2\2#\u0115\3\2\2\2%\u0118\3\2\2\2")
        buf.write("\'\u0122\3\2\2\2)\u0129\3\2\2\2+\u012e\3\2\2\2-\u0132")
        buf.write("\3\2\2\2/\u0138\3\2\2\2\61\u013d\3\2\2\2\63\u0143\3\2")
        buf.write("\2\2\65\u0149\3\2\2\2\67\u014b\3\2\2\29\u014e\3\2\2\2")
        buf.write(";\u0150\3\2\2\2=\u0153\3\2\2\2?\u0155\3\2\2\2A\u0158\3")
        buf.write("\2\2\2C\u015a\3\2\2\2E\u015d\3\2\2\2G\u015f\3\2\2\2I\u0161")
        buf.write("\3\2\2\2K\u0164\3\2\2\2M\u0167\3\2\2\2O\u016a\3\2\2\2")
        buf.write("Q\u016d\3\2\2\2S\u016f\3\2\2\2U\u0171\3\2\2\2W\u0174\3")
        buf.write("\2\2\2Y\u0177\3\2\2\2[\u017b\3\2\2\2]\u017e\3\2\2\2_\u0181")
        buf.write("\3\2\2\2a\u0185\3\2\2\2c\u0189\3\2\2\2e\u018b\3\2\2\2")
        buf.write("g\u018d\3\2\2\2i\u018f\3\2\2\2k\u0191\3\2\2\2m\u0193\3")
        buf.write("\2\2\2o\u0195\3\2\2\2q\u0197\3\2\2\2s\u0199\3\2\2\2u\u019b")
        buf.write("\3\2\2\2w\u019d\3\2\2\2y\u019f\3\2\2\2{\u01af\3\2\2\2")
        buf.write("}\u01f8\3\2\2\2\177\u01fa\3\2\2\2\u0081\u01fc\3\2\2\2")
        buf.write("\u0083\u020d\3\2\2\2\u0085\u021e\3\2\2\2\u0087\u0227\3")
        buf.write("\2\2\2\u0089\u022f\3\2\2\2\u008b\u0239\3\2\2\2\u008d\u023b")
        buf.write("\3\2\2\2\u008f\u0241\3\2\2\2\u0091\u0243\3\2\2\2\u0093")
        buf.write("\u024d\3\2\2\2\u0095\u0257\3\2\2\2\u0097\u0263\3\2\2\2")
        buf.write("\u0099\u026d\3\2\2\2\u009b\u009f\t\2\2\2\u009c\u009e\t")
        buf.write("\3\2\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\4\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a2\u00ad\t\4\2\2\u00a3\u00a7\5\177@\2\u00a4")
        buf.write("\u00a6\5}?\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00ad\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00aa\u00ad\5\u0081A\2\u00ab\u00ad")
        buf.write("\5\u0083B\2\u00ac\u00a2\3\2\2\2\u00ac\u00a3\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\6\3\2\2\2\u00ae")
        buf.write("\u00b1\5/\30\2\u00af\u00b1\5\61\31\2\u00b0\u00ae\3\2\2")
        buf.write("\2\u00b0\u00af\3\2\2\2\u00b1\b\3\2\2\2\u00b2\u00b4\5}")
        buf.write("?\2\u00b3\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7")
        buf.write("\u00b9\5\u0087D\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2")
        buf.write("\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\5\u0085C\2\u00bb")
        buf.write("\u00c6\3\2\2\2\u00bc\u00be\5}?\2\u00bd\u00bc\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2")
        buf.write("\u00c0\u00c1\3\2\2\2\u00c1\u00c3\5\u0087D\2\u00c2\u00c4")
        buf.write("\5\u0085C\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\u00c6\3\2\2\2\u00c5\u00b3\3\2\2\2\u00c5\u00bd\3\2\2\2")
        buf.write("\u00c6\n\3\2\2\2\u00c7\u00c8\7D\2\2\u00c8\u00c9\7q\2\2")
        buf.write("\u00c9\u00ca\7f\2\2\u00ca\u00cb\7{\2\2\u00cb\f\3\2\2\2")
        buf.write("\u00cc\u00cd\7D\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7g")
        buf.write("\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7m\2\2\u00d1\16\3")
        buf.write("\2\2\2\u00d2\u00d3\7E\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da\7g\2\2\u00da\20")
        buf.write("\3\2\2\2\u00db\u00dc\7F\2\2\u00dc\u00dd\7q\2\2\u00dd\22")
        buf.write("\3\2\2\2\u00de\u00df\7G\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1")
        buf.write("\7u\2\2\u00e1\u00e2\7g\2\2\u00e2\24\3\2\2\2\u00e3\u00e4")
        buf.write("\7G\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7\u00e8\7K\2\2\u00e8\u00e9\7h\2\2\u00e9\26")
        buf.write("\3\2\2\2\u00ea\u00eb\7G\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed")
        buf.write("\7f\2\2\u00ed\u00ee\7D\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0")
        buf.write("\7f\2\2\u00f0\u00f1\7{\2\2\u00f1\30\3\2\2\2\u00f2\u00f3")
        buf.write("\7G\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7f\2\2\u00f5\u00f6")
        buf.write("\7K\2\2\u00f6\u00f7\7h\2\2\u00f7\32\3\2\2\2\u00f8\u00f9")
        buf.write("\7G\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7f\2\2\u00fb\u00fc")
        buf.write("\7H\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7t\2\2\u00fe\34")
        buf.write("\3\2\2\2\u00ff\u0100\7G\2\2\u0100\u0101\7p\2\2\u0101\u0102")
        buf.write("\7f\2\2\u0102\u0103\7Y\2\2\u0103\u0104\7j\2\2\u0104\u0105")
        buf.write("\7k\2\2\u0105\u0106\7n\2\2\u0106\u0107\7g\2\2\u0107\36")
        buf.write("\3\2\2\2\u0108\u0109\7H\2\2\u0109\u010a\7q\2\2\u010a\u010b")
        buf.write("\7t\2\2\u010b \3\2\2\2\u010c\u010d\7H\2\2\u010d\u010e")
        buf.write("\7w\2\2\u010e\u010f\7p\2\2\u010f\u0110\7e\2\2\u0110\u0111")
        buf.write("\7v\2\2\u0111\u0112\7k\2\2\u0112\u0113\7q\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\"\3\2\2\2\u0115\u0116\7K\2\2\u0116\u0117")
        buf.write("\7h\2\2\u0117$\3\2\2\2\u0118\u0119\7R\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7t\2\2\u011b\u011c\7c\2\2\u011c\u011d")
        buf.write("\7o\2\2\u011d\u011e\7g\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\7t\2\2\u0121&\3\2\2\2\u0122\u0123")
        buf.write("\7T\2\2\u0123\u0124\7g\2\2\u0124\u0125\7v\2\2\u0125\u0126")
        buf.write("\7w\2\2\u0126\u0127\7t\2\2\u0127\u0128\7p\2\2\u0128(\3")
        buf.write("\2\2\2\u0129\u012a\7V\2\2\u012a\u012b\7j\2\2\u012b\u012c")
        buf.write("\7g\2\2\u012c\u012d\7p\2\2\u012d*\3\2\2\2\u012e\u012f")
        buf.write("\7X\2\2\u012f\u0130\7c\2\2\u0130\u0131\7t\2\2\u0131,\3")
        buf.write("\2\2\2\u0132\u0133\7Y\2\2\u0133\u0134\7j\2\2\u0134\u0135")
        buf.write("\7k\2\2\u0135\u0136\7n\2\2\u0136\u0137\7g\2\2\u0137.\3")
        buf.write("\2\2\2\u0138\u0139\7V\2\2\u0139\u013a\7t\2\2\u013a\u013b")
        buf.write("\7w\2\2\u013b\u013c\7g\2\2\u013c\60\3\2\2\2\u013d\u013e")
        buf.write("\7H\2\2\u013e\u013f\7c\2\2\u013f\u0140\7n\2\2\u0140\u0141")
        buf.write("\7u\2\2\u0141\u0142\7g\2\2\u0142\62\3\2\2\2\u0143\u0144")
        buf.write("\7G\2\2\u0144\u0145\7p\2\2\u0145\u0146\7f\2\2\u0146\u0147")
        buf.write("\7F\2\2\u0147\u0148\7q\2\2\u0148\64\3\2\2\2\u0149\u014a")
        buf.write("\7-\2\2\u014a\66\3\2\2\2\u014b\u014c\7-\2\2\u014c\u014d")
        buf.write("\7\60\2\2\u014d8\3\2\2\2\u014e\u014f\7/\2\2\u014f:\3\2")
        buf.write("\2\2\u0150\u0151\7/\2\2\u0151\u0152\7\60\2\2\u0152<\3")
        buf.write("\2\2\2\u0153\u0154\7,\2\2\u0154>\3\2\2\2\u0155\u0156\7")
        buf.write(",\2\2\u0156\u0157\7\60\2\2\u0157@\3\2\2\2\u0158\u0159")
        buf.write("\7^\2\2\u0159B\3\2\2\2\u015a\u015b\7^\2\2\u015b\u015c")
        buf.write("\7\60\2\2\u015cD\3\2\2\2\u015d\u015e\7\'\2\2\u015eF\3")
        buf.write("\2\2\2\u015f\u0160\7#\2\2\u0160H\3\2\2\2\u0161\u0162\7")
        buf.write("(\2\2\u0162\u0163\7(\2\2\u0163J\3\2\2\2\u0164\u0165\7")
        buf.write("~\2\2\u0165\u0166\7~\2\2\u0166L\3\2\2\2\u0167\u0168\7")
        buf.write("#\2\2\u0168\u0169\7?\2\2\u0169N\3\2\2\2\u016a\u016b\7")
        buf.write("?\2\2\u016b\u016c\7?\2\2\u016cP\3\2\2\2\u016d\u016e\7")
        buf.write(">\2\2\u016eR\3\2\2\2\u016f\u0170\7@\2\2\u0170T\3\2\2\2")
        buf.write("\u0171\u0172\7>\2\2\u0172\u0173\7?\2\2\u0173V\3\2\2\2")
        buf.write("\u0174\u0175\7@\2\2\u0175\u0176\7?\2\2\u0176X\3\2\2\2")
        buf.write("\u0177\u0178\7?\2\2\u0178\u0179\7\61\2\2\u0179\u017a\7")
        buf.write("?\2\2\u017aZ\3\2\2\2\u017b\u017c\7>\2\2\u017c\u017d\7")
        buf.write("\60\2\2\u017d\\\3\2\2\2\u017e\u017f\7@\2\2\u017f\u0180")
        buf.write("\7\60\2\2\u0180^\3\2\2\2\u0181\u0182\7>\2\2\u0182\u0183")
        buf.write("\7?\2\2\u0183\u0184\7\60\2\2\u0184`\3\2\2\2\u0185\u0186")
        buf.write("\7@\2\2\u0186\u0187\7?\2\2\u0187\u0188\7\60\2\2\u0188")
        buf.write("b\3\2\2\2\u0189\u018a\7?\2\2\u018ad\3\2\2\2\u018b\u018c")
        buf.write("\7]\2\2\u018cf\3\2\2\2\u018d\u018e\7_\2\2\u018eh\3\2\2")
        buf.write("\2\u018f\u0190\7}\2\2\u0190j\3\2\2\2\u0191\u0192\7\177")
        buf.write("\2\2\u0192l\3\2\2\2\u0193\u0194\7*\2\2\u0194n\3\2\2\2")
        buf.write("\u0195\u0196\7+\2\2\u0196p\3\2\2\2\u0197\u0198\7<\2\2")
        buf.write("\u0198r\3\2\2\2\u0199\u019a\7=\2\2\u019at\3\2\2\2\u019b")
        buf.write("\u019c\7\60\2\2\u019cv\3\2\2\2\u019d\u019e\7.\2\2\u019e")
        buf.write("x\3\2\2\2\u019f\u01a0\7,\2\2\u01a0\u01a1\7,\2\2\u01a1")
        buf.write("\u01a7\3\2\2\2\u01a2\u01a6\n\5\2\2\u01a3\u01a4\7,\2\2")
        buf.write("\u01a4\u01a6\n\5\2\2\u01a5\u01a2\3\2\2\2\u01a5\u01a3\3")
        buf.write("\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa")
        buf.write("\u01ab\7,\2\2\u01ab\u01ac\7,\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("\u01ae\b=\2\2\u01aez\3\2\2\2\u01af\u01b3\5i\65\2\u01b0")
        buf.write("\u01b2\7\"\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2")
        buf.write("\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01ee\3")
        buf.write("\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b8\7\"\2\2\u01b7\u01b6")
        buf.write("\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01c1\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bc\u01c2\5{>\2\u01bd\u01c2\5\5\3\2\u01be\u01c2\5\t")
        buf.write("\5\2\u01bf\u01c2\5\7\4\2\u01c0\u01c2\5\u0091I\2\u01c1")
        buf.write("\u01bc\3\2\2\2\u01c1\u01bd\3\2\2\2\u01c1\u01be\3\2\2\2")
        buf.write("\u01c1\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c6\3")
        buf.write("\2\2\2\u01c3\u01c5\7\"\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8")
        buf.write("\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7")
        buf.write("\u01e5\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01cb\7\"\2\2")
        buf.write("\u01ca\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3")
        buf.write("\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc")
        buf.write("\3\2\2\2\u01cf\u01d3\5w<\2\u01d0\u01d2\7\"\2\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01db\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d6\u01dc\5\5\3\2\u01d7\u01dc\5\t\5\2\u01d8\u01dc\5")
        buf.write("\7\4\2\u01d9\u01dc\5\u0091I\2\u01da\u01dc\5{>\2\u01db")
        buf.write("\u01d6\3\2\2\2\u01db\u01d7\3\2\2\2\u01db\u01d8\3\2\2\2")
        buf.write("\u01db\u01d9\3\2\2\2\u01db\u01da\3\2\2\2\u01dc\u01e0\3")
        buf.write("\2\2\2\u01dd\u01df\7\"\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2")
        buf.write("\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1")
        buf.write("\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01cc\3\2\2\2")
        buf.write("\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3")
        buf.write("\2\2\2\u01e6\u01eb\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01ea")
        buf.write("\7\"\2\2\u01e9\u01e8\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb")
        buf.write("\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ef\3\2\2\2")
        buf.write("\u01ed\u01eb\3\2\2\2\u01ee\u01b9\3\2\2\2\u01ee\u01ef\3")
        buf.write("\2\2\2\u01ef\u01f3\3\2\2\2\u01f0\u01f2\7\"\2\2\u01f1\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3")
        buf.write("\u01f4\3\2\2\2\u01f4\u01f6\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f6\u01f7\5k\66\2\u01f7|\3\2\2\2\u01f8\u01f9\t\6\2")
        buf.write("\2\u01f9~\3\2\2\2\u01fa\u01fb\t\7\2\2\u01fb\u0080\3\2")
        buf.write("\2\2\u01fc\u01fe\7\62\2\2\u01fd\u01ff\t\b\2\2\u01fe\u01fd")
        buf.write("\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u0201\3\2\2\2\u0201\u0203\3\2\2\2\u0202\u0204\t\t\2\2")
        buf.write("\u0203\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0205\u0206\3\2\2\2\u0206\u020a\3\2\2\2\u0207\u0209")
        buf.write("\t\n\2\2\u0208\u0207\3\2\2\2\u0209\u020c\3\2\2\2\u020a")
        buf.write("\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u0082\3\2\2\2")
        buf.write("\u020c\u020a\3\2\2\2\u020d\u020f\7\62\2\2\u020e\u0210")
        buf.write("\t\13\2\2\u020f\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0214\3\2\2\2")
        buf.write("\u0213\u0215\t\f\2\2\u0214\u0213\3\2\2\2\u0215\u0216\3")
        buf.write("\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u021b")
        buf.write("\3\2\2\2\u0218\u021a\t\r\2\2\u0219\u0218\3\2\2\2\u021a")
        buf.write("\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2")
        buf.write("\u021c\u0084\3\2\2\2\u021d\u021b\3\2\2\2\u021e\u0220\t")
        buf.write("\16\2\2\u021f\u0221\t\17\2\2\u0220\u021f\3\2\2\2\u0220")
        buf.write("\u0221\3\2\2\2\u0221\u0223\3\2\2\2\u0222\u0224\5}?\2\u0223")
        buf.write("\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0223\3\2\2\2")
        buf.write("\u0225\u0226\3\2\2\2\u0226\u0086\3\2\2\2\u0227\u022b\7")
        buf.write("\60\2\2\u0228\u022a\5}?\2\u0229\u0228\3\2\2\2\u022a\u022d")
        buf.write("\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c")
        buf.write("\u0088\3\2\2\2\u022d\u022b\3\2\2\2\u022e\u0230\t\20\2")
        buf.write("\2\u022f\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u022f")
        buf.write("\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0233\3\2\2\2\u0233")
        buf.write("\u0234\bE\2\2\u0234\u008a\3\2\2\2\u0235\u023a\n\21\2\2")
        buf.write("\u0236\u0237\7)\2\2\u0237\u023a\7$\2\2\u0238\u023a\5\u008d")
        buf.write("G\2\u0239\u0235\3\2\2\2\u0239\u0236\3\2\2\2\u0239\u0238")
        buf.write("\3\2\2\2\u023a\u008c\3\2\2\2\u023b\u023c\7^\2\2\u023c")
        buf.write("\u023d\t\22\2\2\u023d\u008e\3\2\2\2\u023e\u023f\7^\2\2")
        buf.write("\u023f\u0242\n\22\2\2\u0240\u0242\7)\2\2\u0241\u023e\3")
        buf.write("\2\2\2\u0241\u0240\3\2\2\2\u0242\u0090\3\2\2\2\u0243\u0247")
        buf.write("\7$\2\2\u0244\u0246\5\u008bF\2\u0245\u0244\3\2\2\2\u0246")
        buf.write("\u0249\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2")
        buf.write("\u0248\u024a\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b\7")
        buf.write("$\2\2\u024b\u024c\bI\3\2\u024c\u0092\3\2\2\2\u024d\u0251")
        buf.write("\7$\2\2\u024e\u0250\5\u008bF\2\u024f\u024e\3\2\2\2\u0250")
        buf.write("\u0253\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2")
        buf.write("\u0252\u0254\3\2\2\2\u0253\u0251\3\2\2\2\u0254\u0255\5")
        buf.write("\u008fH\2\u0255\u0256\bJ\4\2\u0256\u0094\3\2\2\2\u0257")
        buf.write("\u025b\7$\2\2\u0258\u025a\5\u008bF\2\u0259\u0258\3\2\2")
        buf.write("\2\u025a\u025d\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025c")
        buf.write("\3\2\2\2\u025c\u025f\3\2\2\2\u025d\u025b\3\2\2\2\u025e")
        buf.write("\u0260\t\23\2\2\u025f\u025e\3\2\2\2\u0260\u0261\3\2\2")
        buf.write("\2\u0261\u0262\bK\5\2\u0262\u0096\3\2\2\2\u0263\u0264")
        buf.write("\7,\2\2\u0264\u0265\7,\2\2\u0265\u026a\3\2\2\2\u0266\u0267")
        buf.write("\n\5\2\2\u0267\u0269\n\5\2\2\u0268\u0266\3\2\2\2\u0269")
        buf.write("\u026c\3\2\2\2\u026a\u0268\3\2\2\2\u026a\u026b\3\2\2\2")
        buf.write("\u026b\u0098\3\2\2\2\u026c\u026a\3\2\2\2\u026d\u026e\13")
        buf.write("\2\2\2\u026e\u026f\bM\6\2\u026f\u009a\3\2\2\2+\2\u009f")
        buf.write("\u00a7\u00ac\u00b0\u00b5\u00b8\u00bf\u00c3\u00c5\u01a5")
        buf.write("\u01a7\u01b3\u01b9\u01c1\u01c6\u01cc\u01d3\u01db\u01e0")
        buf.write("\u01e5\u01eb\u01ee\u01f3\u0200\u0205\u020a\u0211\u0216")
        buf.write("\u021b\u0220\u0225\u022b\u0231\u0239\u0241\u0247\u0251")
        buf.write("\u025b\u025f\u026a\7\b\2\2\3I\2\3J\3\3K\4\3M\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    INT_LIT = 2
    BOOLEAN_LIT = 3
    FLOAT_LIT = 4
    BODY = 5
    BREAK = 6
    CONTINUE = 7
    DO = 8
    ELSE = 9
    ELSEIF = 10
    ENDBODY = 11
    ENDIF = 12
    ENDFOR = 13
    ENDWHILE = 14
    FOR = 15
    FUNCTION = 16
    IF = 17
    PARAMETER = 18
    RETURN = 19
    THEN = 20
    VAR = 21
    WHILE = 22
    TRUE = 23
    FALSE = 24
    ENDDO = 25
    ADDINT = 26
    ADDFLOAT = 27
    SUBINT = 28
    SUBFLOAT = 29
    MULINT = 30
    MULFLOAT = 31
    DIVINT = 32
    DIVFLOAT = 33
    MODINT = 34
    NOT = 35
    AND = 36
    OR = 37
    NOT_EQUALINT = 38
    EQUALINT = 39
    LTHANINT = 40
    GTHANINT = 41
    LEQUALINT = 42
    GEQUALINT = 43
    NOT_EQUALFLOAT = 44
    LTHANFLOAT = 45
    GTHANFLOAT = 46
    LEQUALFLOAT = 47
    GEQUALFLOAT = 48
    ASSIGN = 49
    LSB = 50
    RSB = 51
    LB = 52
    RB = 53
    LP = 54
    RP = 55
    COLON = 56
    SEMI = 57
    DOT = 58
    COMMA = 59
    COMMENT = 60
    ARRAY_LIT = 61
    INT = 62
    INT_WITHOUT_0 = 63
    WS = 64
    STRING_LIT = 65
    ILLEGAL_ESCAPE = 66
    UNCLOSE_STRING = 67
    UNTERMINATED_COMMENT = 68
    ERROR_CHAR = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
            "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", 
            "'>.'", "'<=.'", "'>=.'", "'='", "'['", "']'", "'{'", "'}'", 
            "'('", "')'", "':'", "';'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT_LIT", "BOOLEAN_LIT", "FLOAT_LIT", "BODY", "BREAK", 
            "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
            "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
            "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "ADDINT", 
            "ADDFLOAT", "SUBINT", "SUBFLOAT", "MULINT", "MULFLOAT", "DIVINT", 
            "DIVFLOAT", "MODINT", "NOT", "AND", "OR", "NOT_EQUALINT", "EQUALINT", 
            "LTHANINT", "GTHANINT", "LEQUALINT", "GEQUALINT", "NOT_EQUALFLOAT", 
            "LTHANFLOAT", "GTHANFLOAT", "LEQUALFLOAT", "GEQUALFLOAT", "ASSIGN", 
            "LSB", "RSB", "LB", "RB", "LP", "RP", "COLON", "SEMI", "DOT", 
            "COMMA", "COMMENT", "ARRAY_LIT", "INT", "INT_WITHOUT_0", "WS", 
            "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "ID", "INT_LIT", "BOOLEAN_LIT", "FLOAT_LIT", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "ADDINT", "ADDFLOAT", "SUBINT", "SUBFLOAT", "MULINT", 
                  "MULFLOAT", "DIVINT", "DIVFLOAT", "MODINT", "NOT", "AND", 
                  "OR", "NOT_EQUALINT", "EQUALINT", "LTHANINT", "GTHANINT", 
                  "LEQUALINT", "GEQUALINT", "NOT_EQUALFLOAT", "LTHANFLOAT", 
                  "GTHANFLOAT", "LEQUALFLOAT", "GEQUALFLOAT", "ASSIGN", 
                  "LSB", "RSB", "LB", "RB", "LP", "RP", "COLON", "SEMI", 
                  "DOT", "COMMA", "COMMENT", "ARRAY_LIT", "INT", "INT_WITHOUT_0", 
                  "HEX", "OCT", "EXP", "DEC", "WS", "STR_CHAR", "ESCAPE_SEQUENCES", 
                  "ESCAPE_ILLEGAL", "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[71] = self.STRING_LIT_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[75] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text)
                    
                    self.text = y[1:-1]
                  

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    y = str(self.text)
                    
                    raise IllegalEscape(y[1:]) 

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    y = str(self.text)
                    
                    if y[-1] == '\n': 
                            raise UncloseString(y[1:-1])
                    else: 
                            raise UncloseString(y[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             
                    raise ErrorToken(self.text)

     


