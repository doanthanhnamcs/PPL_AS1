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
    def test_para_with_exp_func_decl_1(self):
        """ para exp"""
        input = """ Var: a,b,c,l[0x4332A];
        Function: nam **#$%#$%#$%#$**
        Parameter: rapViet,kingOf_rAp
        Body:
            Var:html,css=3;
            While (x == 1) Do
            If(3<2) Then i=3+2;
            Else
            Break;
            EndIf.
            EndWhile. 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    #####This is complex test ########
    def test_complex_1(self):
        """ Complex"""
        input = """ Var: x[3][3 +. foo(foo(3))];
        Function: nam____ **#$%#$%#$%#$**
        Parameter: k,m,n
        Body:
        EndBody."""
        expect = "Error on line 1 col 13: +."
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_complex_2(self):
        """ Complex"""
        input = """ Var: x[3][0xFFFAA];
        Function: n___Am___hahsdh_
        Parameter:
        Body:
            For(i=3+y,i<5,2) Do
            If(nothing(1)) Then
            If(nothing(2)) Then EndIf.
            EndIf.
            EndFor.
        EndBody."""
        expect = "Error on line 4 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_complex_3(self):
        """ Complex"""
        input = """ Var: x[3][0xFFFAA];
        Function: n___Am___hahsdh_
        Parameter: namngaytho
        Body:
            For(i=3+y,i<5,2) Do
            If(nothing(nothing(nothing(1)))) Then
            If(nothing(2)) Then EndIf.
            EndIf.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_complex_4(self):
        """ Complex"""
        input = """ 
        Function: n__________A_______Mkaka23132141wq123
        Parameter: noneed
        Body:
            Break;
            Break;
            Continue;
            Break;
            Break;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_complex_5(self):
        """ Complex"""
        input = """ 
        Function: n_____123456789_____A_______M
        Body:
            Return;
            Return foo(3+.*.fooooo("abc"));
        EndBody."""
        expect = "Error on line 5 col 26: *."
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_complex_6(self):
        """ Complex"""
        input = """ 
        Var : a,b,c={{1,2,3},{3,4,"String never die"}};
        Function: main
        Body:
            Return;
            Return foo(3-.fooooo("abc"));
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_complex_7(self):
        """ Complex"""
        input = """ 
        
        Function: main
        Body:
            Do
            x=a(x+x(5+x(5)));
            Return 0;
            While (x!=2)
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_complex_8(self):
        """ Complex"""
        input = """ 
        
        Function: main
        BOdy:
            Do
            While
            EndDo.
        EndBody."""
        expect = "B"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_complex_9(self):
        """ Complex"""
        input = """ 
        
        Function: main
        Body:
            Do
            foo(avbsabda__4(4+3*f(5)));
            While(!5) Do
            EndWhile
            Return 0;
            While (x)
            EndDo.
        EndBody."""
        expect = "Error on line 9 col 12: Return"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_complex_10(self):
        """ Complex"""
        input = """ 
        
        Function: main
        Body:
           a=b+3;
           Var:x=5,y=9;
        EndBody."""
        expect = "Error on line 6 col 11: Var"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_complex_11(self):
        """ Complex"""
        input = """ 
        Var:m[1231],n[0xF6A]={"haha",123};
        Function: main_____________
        Parameter:a,b,cdef
        Body:
           Do **nothing**
           Var:x=3;
           While(y>4)
           EndDo.
        EndBody."""
        expect = "Error on line 7 col 11: Var"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_complex_12(self):
        """ Complex"""
        input = """ 
        Var:x,y,z;
        Function: n_____
        Body:
           Var: a[a[1]] = 1;
        EndBody."""
        expect = "Error on line 5 col 18: a"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_complex_13(self):
        """ Complex"""
        input = """ 
        Var: m, n[10]; 
            Function: main 
           
                Parameter: n 
                Body: 
                x = 12e+4444;
               If n =/= 0 Then 
                   Return 1; 
               Else    Return n*main({4,5});
                EndIf.
                 EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_complex_14(self):
        """ Complex"""
        input = """ 
        Function:main
        Body:
        Var: i = 5;
        While(i>0) Do
        print(print(print(i)));
        Continue;
        EndWhile.
        EndBody.
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_complex_15(self):
        """ Complex"""
        input = """ 
        Function:main
        Body:
        Var: i = 5;
        While(i>0) Do
        print(print(print(i)));
        Continue;
        EndWhile.
        EndBody.
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_complex_16(self):
        """ Complex"""
        input = """ 
        Function: ma__ABCDEFin
         Body:
             asm =  1 +.-.---"abc"*12.e+400;
            While (print({4,5,6}) = 123, i < 1e9, 10)
                tttttttest();
            EndWhile.
                     EndBody.
         """
        expect = "Error on line 5 col 34: ="
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_complex_17(self):
        """ Complex"""
        input = """ 
        Function: ma__ABCDE____Fin
         Body:
            foo(print(ggwp({{1,2,3},{"abC:???"}})));
            Continue;
            Break;Continue;
            Break;Continue;
            Break;Continue;
            Break;
                     EndBody.
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_complex_18(self):
        """ Complex"""
        input = """ 
        Var: x,a,bcd;
        Function: nam
        Parameter: m[5],n[100]
        Body:
            Var:k,j;
            x=a(5)[6][0xFA][0o44];
        EndBody.
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_complex_19(self):
        """ Complex"""
        input = """ 
        Var: x="?#!@!$!@$!",y=5,z=12.6,k={"@#$@#$@dsadjkhasdjkhas"};
        Function: ma___F__in
        Parameter: m[5] =6;
         Body:
            Break;
            Break;
            Break;
            Break;
        EndBody.
         """
        expect = "Error on line 4 col 24: ="
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_complex_20(self):
        """ Complex"""
        input = """ 
        **Var: x="?#!@!$!@$!",y=5,****z=12.6,k={"@#$@#$@dsadjkhasdjkhas"};**
        Function: noname
        Parameter: x
         Body:
            Return;
            Return;
            Return;
            Return;
            Return;
        EndBody.
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_complex_21(self):
        """ Complex"""
        input = """ 
        Var: a,b,c;
        Function: n_o_n_a_m_e
        Parameter: none
         Body:
            If(i == 1) Then print(i);print(i);print(i);print(i);print(i);print(i);
        EndBody.
         """
        expect = "Error on line 7 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_complex_22(self):
        """ Complex"""
        input = """ 
        Var: a,b,c;
        Function: n_o_n_a_m_e
        Parameter: none
         Body:
            If(i == 1) Then print(i);print(i);print(i);print(i);print(i);print(i);
            EndIf.
        EndBody.
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_complex_23(self):
        """ Complex"""
        input = """ 
        Var: a,b,c;
        Function: nam_1813130
        Parameter: parameter
         Body:
            Return 1+2;
            Return 1+2,{"$@#$@!SADASDASDFakjgshduhgu2_2901309813"};
        EndBody.
         """
        expect = "Error on line 7 col 22: ,"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_complex_24(self):
        """ Complex"""
        input = """ 
        
        Function: nam_1813130
         Body:
            x = y =/= True +. --. -----* 5;
        EndBody.
         """
        expect = "Error on line 5 col 39: *"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_complex_25(self):
        """ Complex"""
        input = """ 
        
        Function: main
         Body:
         Do
            x = 9 == 6 == y =/= 5;
            While(!!!!False)
        EndDo.
        EndBody.
         """
        expect = "Error on line 6 col 23: =="
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_complex_26(self):
        """ Complex"""
        input = """ 
        Var: x = "%%%%%%%%%", y = 6 , m[0o1111] = 1e9999;
        Function: mainSDADASD12312132
         Body:
         Var:x,y,z;
         While(!!!!6=/=9)
         Do print(print(print(in(in(i)))));
         EndWhile.
        EndBody.
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_complex_27(self):
        """ Complex"""
        input = """ 
        Function: mainSDAD
         Body:
            Parameter:x
            print(hello);
        EndBody.
         """
        expect = "Error on line 4 col 12: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_complex_28(self):
        """ Complex"""
        input = """ 
        Var: x = "\b\b\b\b\b", y = 6e444 , m[0o1111];
        Function: nam__t_h_y
         Body:
            **do nothing**
        EndBody.
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_complex_29(self):
        """ Complex"""
        input = """ 
        Var: a,b,c;
        Function: nam__t_h
        Parameter: hello, hi ** unterminated comment
         Body:
            i=i+1;
        EndBody.
         """
        expect = ""
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_complex_30(self):
        """ Complex"""
        input = """Var: a[5] = {"$@#$@#$@@#$____",2} ; 
        Function: a
        Parameter: f
        Body: 
            Var: a = {1,2,3}, b = "abc"; 
            foo(arr[5] *. 5 * foo("abc"),True,"abc"); 
            If (h * 5 && k && t + 8) Then a = 1; ElseIf e >=. 8 Then x=y+1; EndIf. 
            Do 
                a = a[5]; 
                If arr[5][9+foo(8)*2] Then **nothing**
            While c --------- 5
            EndDo.   
        EndBody.
        """
        expect = "Error on line 12 col 12: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_complex_31(self):
        """ Complex"""
        input = """Var: a[5] = {"$@#$@____#$@@#$____",2} ; 
        Function: nam
        Parameter: f_____,m[1000]
        Body: 
            foo(arr[5] *. 5 * foo("abc"),True,"abc"); 
            Return;
            Return;
            Break;
            Var: a = {1,2,3}, b = "abc"; 
              
        EndBody.
        """
        expect = "Error on line 9 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_complex_32(self):
        """ Complex"""
        input = """Var: kkk[5][6]="@#!$!@$!!!!!",a=0.e+4 ;
        Function: nam
        Parameter: n[100],m[1000]
        Body: 
             thread_multi = 9 > 6 < 2;
        EndBody.
        """
        expect = "Error on line 5 col 34: <"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_complex_33(self):
        """ Complex"""
        input = """
        Function: nAm
        Parameter: n[100],m[1000]
        Body: 
            Var: kkk[5][6]="@#!$!@$!!!!!",a=0.e+4 ;
            Var: kkk[5][6]="@#!$!@$!!!!!",a=0.e+4 ;
            Var: kkk[5][6]="@#!$!@$!!!!!",a=0.e+4 ;
            c= c(**555555**)+ a[0xBCD];
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_complex_34(self):
        """ Complex"""
        input = """
        Function: nAm___
        Parameter: n[100],m[1000];
        Body: 
            **non body**
        EndBody.
        """
        expect = "Error on line 3 col 33: ;"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_complex_35(self):
        """ Complex"""
        input = """
        Function: nAm___
        Parameter: n[100],m[1000]
        Body: 
            foo(2. +. 4., 2 *. 10,c(in(in(in4))));
            Do While(x<3) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_complex_36(self):
        """ Complex"""
        input = """
        Function: nAm___
        Parameter: n[100],m[1000]
        Body: 
        Var: x = "__@#!@#!R@#!@!@SDASFf",b=312312312313.e+4444444444;
            foo(2. +. 4., 2 *. 10,c(in(in(in4))));
            foo(2. +. 4., 2 *. 10,c(in(in(in4))));
            foo(2. +. 4., 2 *. 10,c(in(in(in4))));
            foo(2. +. 4., 2 *. 10,c(in(in(in4))));
            Do While() EndDo.
        EndBody.
        """
        expect = "Error on line 10 col 21: )"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_complex_37(self):
        """ Complex"""
        input = """
        Function: nAm___
        Parameter: n[100],m[1000]
        Body: 
            **test somthing**
            x = (foo(foo(a[5]+"abc")))[2][3];
        EndBody.
        """
        expect = "Error on line 6 col 38: ["
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_complex_38(self):
        """ Complex"""
        input = """
        Function: n____Am___
        Parameter: x,y,z
        Body: 
            theUndertaker = 123*"zzz\z"+-------.-.-.-."theasld**bcd**";
        EndBody.
        """
        expect = "zzz\z"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_complex_39(self):
        """ Complex"""
        input = """
        Function: fact
        Body:
        a[foo(3*foo(3))]= a[1+foo(3)[5]]; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_complex_40(self):
        """ Complex"""
        input = """
        Var:a,b,c;
        Function: fact
        Parameter:x,y,z
        Body:
            foo(2)=123;
        EndBody.
        """
        expect = "Error on line 6 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_complex_41(self):
        """ Complex"""
        input = """
        Var:a,b,c;
        Function: fact
        Parameter:x,y,z
        Body:
        Var: sadasd=4455;
            While(x>3) Do
                If(False) Then 
                ElseIf(!!!a) Then
                Else
                    For(i=0xFF,i<5,1) Do
                    **no thing**
                    EndFor.
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_complex_42(self):
        """ Complex"""
        input = """
        Var:a,b,c;
        Function: fact
        Parameter:x,y,z
        Body:
        Var: sad____asd=4455;
            While(x>3) Do
                If(False) Then 
                Return;
                ElseIf(!!!a) Then
                Break;
                Else
                    For(i=0xFF,i<5,1) Do
                    **no thing**
                    Continue;
                    Break;
                    Return {1,2,3};
                    EndFor.
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_complex_43(self):
        """ Complex"""
        input = """
        Var:a,b,c;
        Function: fact
        **Block comment
        *abc
        *xyz
        *jqk
        **
        Parameter:x,y,z
        Body:
        Var: sad____asd=4455;
            While(x>3) Do
                a=(1+2-.--\---4 || True && False);
                If(False) Then 
                Return;
                ElseIf(!!!a) Then
                Break;
                Else
                    For(i=0xFF,i<5,1) Do
                    **no thing**
                    Continue;
                    Break;
                    Return {1,2,3};
                    EndFor.
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "Error on line 13 col 26: \\"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_complex_44(self):
        """ Complex"""
        input = """
        Var:a,b,c;
        Function: fact
        **hello**
        **world**
        Parameter:f(f(f(f(f("ooo")))))
        Body:
        Var: a________;
            
        EndBody.
        """
        expect = "Error on line 6 col 19: ("
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_complex_45(self):
        """ Complex"""
        input = """
        Var:a__11_22[3]={1,2,"#@$@#$2"};
        Function: fact_1
        
        Parameter:f,f,f,f,f
        Body:
        If "**hello**" Then
        inxxx= 128983 - 4234 +. 43223.55e+4 || !!!!False;
        inpa231 = {123, 435, 423} * in;
        EndIf.
            
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_complex_46(self):
        """ Complex"""
        input = """
        Var:a__11_22[3]={1,2,"#@$@#$2"};
        Function: fact_1
        Body:
            print(a);
        EndBody.
        Function: fact_2
        Body:
            print(a__);
        EndBody.
        Function: fact_3
        Body:
            {}
        EndBody.
        """
        expect = "Error on line 13 col 12: {"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_complex_47(self):
        """ Complex"""
        input = """
        Var:a__11_22[3]={1,2,"#@$@#$2"};
        Function: fact_1
        Parameter: x
        Body:
            print(a);
            Function: fact_2
                Body:
            print(a);
                EndBody.
        EndBody.
        
        """
        expect = "Error on line 7 col 12: Function"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_complex_48(self):
        """ Complex"""
        input = """
                Function: main
        Body:
            While 0xFFF Do
                Do 
                    If i = 1 Then
                        i = "********";
                    EndIf.
                While True EndDo.
            EndWhile.
        EndBody.
        
        """
        expect = "Error on line 6 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_complex_49(self):
        """ Complex"""
        input = """
        Function: main
        **wrong comment ***
        Body:
            
        EndBody.
        
        """
        expect = "Error on line 3 col 26: *"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_complex_50(self):
        """ Complex"""
        input = """
        Function: main
        **good comment **
        Body:
            If(x == (2==1)) =/= 3 Then foo(3);
            EndIf.
        EndBody.
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_complex_51(self):
        """ Complex"""
        input = """
        Function: main
        **good comment **
        Body:
            If(x == (2==1)) =/= 3 Then 
            x = (4 +. True * "abcy#$@@#$" --.-- (5\\foo(2)));
            EndIf.
        EndBody.
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_complex_52(self):
        """ Complex"""
        input = """
        Var : x = -3, y = -12.e004;
        Function: main
        **good comment **
        Body:
            If(x == (2==1)) =/= 3 Then 
            x = (4 +. True * "abcy#$@@#$" --.-- (5\\foo(2)));
            EndIf.
        EndBody.
        
        """
        expect = "Error on line 2 col 18: -"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_complex_53(self):
        """ Complex"""
        input = """
        Var : x = 3, y = 12.e004;
        Function: main
        Body:
             
            x = (4 +. True * "abcy#$@@#$" --.-- (5\\foo(2)[4][5]))[0o66];
            
        EndBody.
        
        """
        expect = "Error on line 6 col 65: ["
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_complex_54(self):
        """ Complex"""
        input = """
        Var : x = 3, y = 12.e004;
        Function: main
        Body:
        Var : a=1;
             "##$$%%"[3] = 2 ;  
        EndBody.
        
        """
        expect = "Error on line 6 col 13: ##$$%%"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_complex_55(self):
        """ Complex"""
        input = """
        Var : x = 3, y = 12.e004;
        Function: main
        Body:
        **** 
        EndBody.
        Function: main
        Body:
        **a=b;** 
        EndBody.
        Function: main_1
        Body:
         a=b; 
        EndBody.
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_complex_56(self):
        """ Complex"""
        input = """
        Var : x = 3, y = 12.e004;
        Function: main
        Body:
        **** 
        EndBody.
        Function: main
        Body:
         **
         Function: main_1
        Body:
         a=b; 
        EndBody.
        **
        ;; 
        EndBody.
        
        
        """
        expect = "Error on line 15 col 8: ;"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_complex_57(self):
        """ Complex"""
        input = """
        Function: main
        Parameter:a
        Body:
        EndBody.
        Function: main
        Body:
         Function: main_1
        Body:
         a=b; 
        EndBody.
        **
        ;; 
        EndBody.
        
        
        """
        expect = "Error on line 8 col 9: Function"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_complex_58(self):
        """ Complex"""
        input = """
        Function: main
        Parameter:a
        Body:
        **unterminated comment below **
        EndBody.
        Function: main
        Body:
        **
         Function: main_1
        Body:
         a=b; 
        EndBody.
        
        EndBody.
        
        
        """
        expect = ""
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_complex_59(self):
        """ Complex"""
        input = """
        Function: main
        Body:
        a=f(f(f(f(****))));
        EndBody.
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_complex_60(self):
        """ Complex"""
        input = """
        Function: fact
        Parameter: x, a[2]
        Body:
            For (i = 0, i < 10, 2) Do
                If (x) Then Break; EndIf.
            EndFor.
            If (x) Then Break; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    def test_complex_61(self):
        """ Complex"""
        input = """
        Function: fact
        Parameter: x, a[2]
        Body:
            {1,2,3}[4]= 1e4;
        EndBody.
        """
        expect = "Error on line 5 col 12: {"
        self.assertTrue(TestParser.checkParser(input,expect,301))