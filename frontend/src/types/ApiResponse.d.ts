type TestCase = {
  expects: string[];
  steps: string[];
  test: string;
};

type APIResponse = {
  results: TestCase[];
  story: string;
};