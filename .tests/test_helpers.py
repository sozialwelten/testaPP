# Test HttpUrl string type
from ..testapp.utils.helpers import HttpUrl

def test_httpurl(*args: str):
    print(":: Test of \"HttpUrl\"..")
    print(":: doc string..")
    for line in (HttpUrl.__doc__ or "").split("\n"):
        print("\t.." + line)

    for i, arg in enumerate(args):
        print(f":: #{i}: \"{arg}\"" )
        try:
            test = HttpUrl(arg)
            print(f"> [method/domain]: f{test.domain()}")
            print(f"> [method/base]: f{test.base_url(True)}")
            print(f"> [method/update]: f{test.update("updatetest")}")
            print(f"> [attr/LOCAL]: f{test.LOCAL}")
        except Exception as e:
            print("!! ERROR: " + str(e))

    print("> [classmethod/makelocal]" + HttpUrl.makelocal())

if __name__ == "__main__":
    test_httpurl("https://ifwo.eu", "https://mulus.science/posts", "http://www.kzu.de")
