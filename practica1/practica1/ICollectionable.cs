using System.Collections;

namespace practica1;

public interface ICollectionable
{
    int Id
    {
        get;
        set;
    }
    bool Contain(string s);
    string[] GetFields();
    Hashtable Errors();
    void create(Hashtable args);
    bool IsValid();
}