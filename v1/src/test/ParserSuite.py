import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_var_decl(self):
        """Simple var_decl """
        input = """
        Var: x,y,z;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,200))
    def test_complex_var_decl_1(self):
        """Complex var_decl """
        input = """
        Var: x=12.4,y,z=5;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))   
    def test_complex_var_decl_2(self):
        """Complex var_decl """
        input = """
        Var: a={1,2,3},c=2.0e4,g=2,f;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))  
    def test_complex_var_decl_3(self):
        """Complex var_decl """
        input = """
        Var: a[2][3]={{2,3,4},{5,6,7}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))   
    def test_complex_var_decl_4(self):
        """Complex var_decl """
        input = """
        Var: a=\"hello\",b=0.0e4,c=25,d={0};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204)) 
    def test_errortype_var_decl(self):
        """ error type """
        input = """
        Var: _wrong = 5;
        """
        expect = "_"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_errortype_var_decl_1(self):
        """ error type """
        input = """
        Var: \"x\"=55;
        """
        expect = "Error on line 2 col 13: x"
        self.assertTrue(TestParser.checkParser(input,expect,206)) 
    def test_errortype_var_decl_2(self):
        """ error type in init value """
        input = """
        Var: x=a;
        """
        expect = "Error on line 2 col 15: a"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_errortype_var_decl_3(self):
        """ error type in init value """
        input = """
        Var: 3=a;
        """
        expect = "Error on line 2 col 13: 3"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_missingkey_var_decl(self):
        """ missing key ;"""
        input = """
        Var : a=4
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_wrongkey_var_decl(self):
        """ wrong key """
        input = """
        var : a=4;
        """
        expect = "Error on line 2 col 8: var"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_missingkey_var_decl_1(self):
        """ missing key :"""
        input = """
        Var  a=4;
        """
        expect = "Error on line 2 col 13: a"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_simple_func_decl(self):
        """ simple func_decl"""
        input = """
        Function: nam
        Parameter: x
        Body:
            x=x+5;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_simple_func_decl_1(self):
        """ simple func_decl"""
        input = """
        Function: nam
        Parameter: x,y,a[20]
        Body:
            y=x*2;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_nonpara_func_decl(self):
        """ nonpara func_decl"""
        input = """
        Function: nam
        **Parameter: x,y,a[20]**
        Body:
            y=x*2;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    
    def test_nonstm_func_decl(self):
        """ nonstm func_decl"""
        input = """
        Function: nam
        **Parameter: x,y,a[20]**
        Body:
           ** y=x*2; **
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_noname_func_decl(self):
        """ noname func_decl"""
        input = """
        Function:
        Parameter: x,y,a[20]
        Body:
            y=x*2; 
        EndBody.
        """
        expect = "Error on line 3 col 8: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_complexstm_func_decl(self):
        """ complex stm in body func_decl"""
        input = """
        Function: nam
        Parameter: x,y,a[20]
        Body:
            y=x*2;
            foo(5);
            a[6]=5*foo(4);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_complexstm_func_decl(self):
        """ complex stm in body func_decl"""
        input = """
        Function: nam
        Parameter: x,y,a[20]
        Body:
            y=x>2;
            foo(5);
            a[6]=5*foo(4);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_complexstm_func_decl(self):
        """ complex stm in body func_decl"""
        input = """
        Function: nam
        Parameter: x,y,a[20]
        Body:
            While ((x != 2) && (y \\ 3)) Do **nothing**
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_complexstm_func_decl_1(self):
        """ fail complex stm in body func_decl"""
        input = """
        Function: nam
        Parameter: x,y,a[20]
        Body:
            While ((x != 2) && (y \\ 3)) Do **nothing**

        EndBody.
        """
        expect = "Error on line 7 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_complexstm_func_decl_2(self):
        """ more complex stm in body func_decl"""
        input = """
        Function: nam
        Parameter: x,y,a[20]
        Body:
            If(abcxyz == them) Then
                For(i=2,i<9,a+2) Do
                x=x+y;
                EndFor.
            ElseIf (True) Then
                **do nothing**
            Else 
            a=b+d;
            foo(2);
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_unbinary_func_decl(self):
        """ unary or binary in body func_decl"""
        input = """
        Function: nam
        Parameter: x,y,a[20]
        Body:
            a=-a;
            a=1+2;
            b=!a;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_unbinary_func_decl_1(self):
        """ unary or binary in body func_decl"""
        input = """
        Function: nam
        Body:
            If(9==4+5 && !b || (a =/= b) ) Then a=2;
            ElseIf (a>b) Then
            **do nothing**
            Else
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_unbinary_func_decl_2(self):
        """ unary or binary in body func_decl"""
        input = """
        Function: nam
        Body:
            For(a9=0xFFFF,b<5,d+.3e4) Do
            foo(4+.5*.r*.r);
            Return (!x);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_unbinary_func_decl_3(self):
        """ unary or binary in body func_decl with wrong operator"""
        input = """
        Function: nam
        Body:
            If(a ? b) Then
            EndIf.
        EndBody.
        """
        expect = "?"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_unbinary_func_decl_3(self):
        """ unary or binary in body func_decl with wrong operator"""
        input = """
        Function: nam
        Body:
            If(a = b) Then
            EndIf.
        EndBody.
        """
        expect = "Error on line 4 col 17: ="
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_unbinary_func_decl_4(self):
        """ unary or binary in body func_decl with wrong operator"""
        input = """
        Function: nam
        Body:
            If(a == b) Then i++4
            EndIf.
        EndBody.
        """
        expect = "Error on line 4 col 29: +"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_C_call_func_decl(self):
        """ Some similiar C call"""
        input = """
        Function: nam
        Body:
            print("Hello World");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_C_call_func_decl_1(self):
        """ Some similiar C call"""
        input = """
        Function: nam
        Parameter: n
        Body:
            If((n % 2) == 0) Then print("even");
            Else print("odd");
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_C_call_func_decl_2(self):
        """ Some similiar C call"""
        input = """
        Function: nam
        Parameter: n
        Body:
            For(i=0,i<n,1) Do
            print(i);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_special_var_decl(self):
        """ Special var_decl"""
        input = """
        Var: foo1(5)[4]={1,2,3};
        """
        expect = "Error on line 2 col 17: ("
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_special_var_decl_1(self):
        """ Special var_decl"""
        input = """
        Var: \"a\"[4]={1,2,3};
        """
        expect = "Error on line 2 col 13: a"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_special_var_decl_2(self):
        """ Special var_decl"""
        input = """
        Var: a[1e4]=1;
        """
        expect = "Error on line 2 col 15: 1e4"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_special_var_decl_3(self):
        """ Special var_decl"""
        input = """
        Var: a[0]=\"abc_xyz\";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_special_exp_func_decl(self):
        """ Special exp"""
        input = """
        Var: x=3,y[5]={\"a\",0e4};
        Function: nam
        Parameter: k,m,n
        Body:
            foo(12.5+True)[4] = \"hello\";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_var_with_exp_func_decl(self):
        """ var exp"""
        input = """
        Var: nam,thy=9+6,hello;
        """
        expect = "Error on line 2 col 22: +"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_var_with_exp_func_decl_1(self):
        """ var exp"""
        input = """
        Var: nam,thy=\"thy\",hello=9\\5;
        """
        expect = "Error on line 2 col 34: \\"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_var_with_exp_func_decl_2(self):
        """ var exp"""
        input = """
        Var: nam,thy=\"thy\",hello=9;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_var_with_exp_func_decl_3(self):
        """ var exp"""
        input = """
        Var: nam,thy=thy,hello=9;
        """
        expect = "Error on line 2 col 21: thy"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_para_with_exp_func_decl(self):
        """ para exp"""
        input = """ Var: a,b,c;
        Function: nam
        Parameter: rapViet = 8,y,a[0xFFA]
        Body:
            **do nothing** 
        EndBody."""
        expect = "Error on line 3 col 27: ="
        self.assertTrue(TestParser.checkParser(input,expect,239))

           
    
