using System.Collections;

namespace practica1;

public class VRList<T> where T: ICollectionable, new()
{
    private List<T> list = new List<T>();
    
    public List<T> List => list;
    
    public VRList() { }
    public VRList(List<T> list)
    {
        this.list = list;
    }
    
    public void AddDataFromFile(string filePath)
    {
        List<T> newRecords = new List<T>();
        using (StreamReader sr = new StreamReader(filePath))
        {
            while (!sr.EndOfStream)
            {
                AddFromLine(sr.ReadLine());
            }
        }
    }

    public bool AddFromLine(string line)
    {
        Hashtable kargs = ReadFromLine(line);
        T vr = new T();
        vr.create(kargs);
        if (vr.IsValid())
        {
            if (uniqueField("Id", vr.Id))
            {
                list.Add(vr);
                return true;
            }
            else
            {
                vr.Errors().Add("Id", $"{vr.Id} must be unique");
            }
        }
        foreach (DictionaryEntry  error in vr.Errors())
        {
            Console.WriteLine(error.Key + " " + error.Value);
        }
        return false;
    }

    public Hashtable ReadFromLine(string line)
    {
        Hashtable kargs = new Hashtable();
        string[] values = line.Split(',');
        var fields = new T().GetFields();
        for (int i = 0; i < fields.Length; i++)
        {
            kargs.Add(fields[i], values[i]);
        }
        return kargs;
    }

    public void PrintAll()
    {
        foreach(var vr in list)
        {
            Console.WriteLine(vr);
        }
    }

    private bool uniqueField(string field, int value)
    {
        if (list.Count > 0)
        {
            foreach (var vr in list)
            {
                if (((int) vr.GetType().GetProperty(field).GetValue(vr)) == value)
                {
                    return false;
                }
            }
        }
        return true;
    }

    public void WriteToFile(string filePath)
    {
        string res = "";
        foreach (var vr in List)
        {
            res += vr.ToString() + "\n";
        }

        try
        {
            File.WriteAllText(filePath, res);
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
    }
    
    public void SortBy(string field)
    {
        list = new List<T>(list.OrderBy(o => o.GetType()
            .GetProperty(field)
            .GetValue(o, null)));
    }
    
    public bool Delete(string val)
    {
        try
        {
            int id = Int32.Parse(val);
            list.RemoveAll(vr => vr.Id == id);
            return true;
        }
        catch (Exception)
        {
            return false;
        }
    }
    
    public VRList<T> Search(string s)
    {
        List<T> result = new List<T>();
        foreach (var vr in list)
        {
            if (vr.Contain(s))
            {
                result.Add(vr);
            }
        }

        return new VRList<T>(result);
    }
    
    public bool Edit(string id)
    {
        try
        {
            int Id = Int32.Parse(id);
            T vr = list.First(l => l.Id == Id);
            list.Remove(vr);
            Console.WriteLine("Input values");
            string str = "Order: ";
            foreach (var field in new T().GetFields())
            {
                str += field + ",";
            }

            Console.WriteLine(str);
            string val = Console.ReadLine();
            if (AddFromLine(val))
            {
                return true;
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
        return false;
    }
    
    
}