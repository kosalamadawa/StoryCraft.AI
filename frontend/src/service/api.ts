export const getPrediction = async (story: string): Promise<APIResponse>  => {
  const url = `https://storycraft.lol/api/v1/predict?text=${story}`;
  const headers = new Headers();
  headers.append("API-KEY", "6d3ff9a5-38a4-41f9-a7c6-9eeff989c531");
  const response = await fetch(encodeURI(url), {
    method: 'GET',
    headers
  });
  const responseJson = await response.json();
  return responseJson;
};

export const getCSV = async (story: string): Promise<Blob> => {
  const url = `https://storycraft.lol/api/v1/predict?text=${story}&is_csv=true`;
  const headers = new Headers();
  headers.append("API-KEY", "6d3ff9a5-38a4-41f9-a7c6-9eeff989c531");
  const response = await fetch(encodeURI(url), {
    method: 'GET',
    headers
  });
  const text = await response.blob();
  return text;
};