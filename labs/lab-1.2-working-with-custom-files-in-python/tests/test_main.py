from  src.main.main import parse_data_object, parse_data


def normalize(s):
    # Remove leading/trailing spaces on each line and ignore empty lines
    return [line.strip() for line in s.strip().splitlines() if line.strip()]

def test_parse_data():
    input_data = """
jobs:
-build:
--docker-image=cimg/base
--steps:
---checkout:
----run=echo "this is the build job"
-test:
--docker-image=cimg/base
--steps:
---checkout:
----run=echo "this is the test job"
""".strip()

    expected = """jobs {
    build {
        docker-image: cimg/base
        steps {
            checkout {
                run: echo "this is the build job"
            }
        }
    },
    test {
        docker-image: cimg/base
        steps {
            checkout {
                run: echo "this is the test job"
            }
        }
    }
}"""
    actual = parse_data(input_data).strip()
    print("ACTUAL:\n", "\n".join(normalize(actual)))
    print("EXPECTED:\n", "\n".join(normalize(expected)))
    assert normalize(actual) == normalize(expected)