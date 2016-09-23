import java.io.*;
class test  
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    
		boolean boo=(args==null)||
		          (new test() 
		           {
		              {
		                test.main(null);
		              }
		             }.equals(null)
		          );
	
		if(boo){
		   System.out.print("a"); 
		}else{
		   System.out.print("b"); 
		}
		
		//System.out.println("boo:"+boo+"    args:"+args);
	}
}
