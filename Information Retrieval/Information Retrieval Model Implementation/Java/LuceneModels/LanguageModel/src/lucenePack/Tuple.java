package lucenePack;

public class Tuple {
	private String name;
	private int data;
	private int index;
	
	public Tuple(String r, int s, int t){
		this.name = r;
		this.data = s;
		this.index = t;
	}
	
	public String getName()
	{
	    return name;
	}

	public void setName(String name)
	{
	    this.name = name;
	}

	public int getData()
	{
	    return data;
	}

	public void setData(int data)
	{
	    this.data = data;
	}

	public int getIndex()
	{
	    return index;
	}

	public void setIndex(int index)
	{
	    this.index = index;
	}


}
