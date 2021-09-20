import java.sql.Array;
import java.util.Arrays;

class Testing{
  
    public static void main(String[]args){

        String s1="abcdefg";
        String s2="ahijk";
        int count=0;
        boolean common=false;
      char[]ch1=s1.toCharArray();
      char[]ch2=s1.toCharArray();
    //   char[]farray1=new char[ch1.length];
    //   char[]farray2=new char[ch2.length];
    //   Arrays.sort(ch1);
    for(int i=0;i<ch1.length;i++){          //i=2
        for(int k=i-1;k>=0;k--){               //k=2
            if(ch1[i]==ch1[k]){           //
                common=true; break;
            }
        }
      if(common==false){
        for(int j=0;j<ch2.length;j++){
            if(ch1[i]==ch2[j]){
                count++;
            }
        }
      }
    }
    System.out.println(count);
        
    }
 
}