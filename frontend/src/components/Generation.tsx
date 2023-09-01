'use client'

import { useEffect, useState } from 'react';
import { getCSV, getPrediction } from '@/service/api';
import { ArrowPathIcon } from '@heroicons/react/24/outline';
import BeatLoader from "react-spinners/BeatLoader";

const Generation: React.FC = () => {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [userStoryInput, setUserStoryInput] = useState<string>('');
  const [testCases, setTestCases] = useState<APIResponse>();
  const [csv, setCsv] = useState<Blob>();

  const onGeneratePress = async (event: any) => {
    event.preventDefault();
    if (userStoryInput !== '') {
      try {
        setIsLoading(true);
        const promisesResponse = await Promise.all([getPrediction(userStoryInput), getCSV(userStoryInput)]);
        setTestCases(promisesResponse[0]);
        setCsv(promisesResponse[1]);
        setIsLoading(false);
      } catch (error) {
        console.error(error);
      }
    };
  };

  useEffect(() => {
    const createExcelLink = (blob: Blob) => {
      const element = document.getElementById('excel-file') as HTMLAnchorElement;
      const url = window.URL.createObjectURL(blob);
      if (element) {
        element.href = url;
        element.download = 'test_cases.xlsx';
      }
    };

    if (csv) {
      createExcelLink(csv);
    }
  }, [csv]);

  const onClearPress = () => {
    setUserStoryInput('');
    setTestCases(undefined);
    setCsv(undefined);
  };

  return (
    <div className="flex flex-1 flex-row justify-between space-x-[20px]">
      <div className="flex flex-1 flex-col items-center">
        <div className="min-h-[350px] h-full w-full bg-gray-800 rounded-[24px] shadow-md border-[1px] border-gray-600">
          <textarea
            className="bg-gray-800 h-full w-full ring-0 outline-0 p-4 rounded-[24px] text-gray-200"
            placeholder="Write the acceptance criteria"
            onChange={(event) => setUserStoryInput(event.target.value)}
            value={userStoryInput}
          />
        </div>
        <div className='flex flex-row space-x-[16px]'>
          <button
            className="w-[197px] h-[40px] flex flex-row justify-center items-center space-x-3 bg-[#3b54d0] text-white shadow-md rounded-[16px] mt-[28px] p-2"
            onClick={onGeneratePress}
            disabled={isLoading}
          >
            {isLoading ? (
              <BeatLoader
                color={'white'}
                loading={isLoading}
                size={12}
              />
            ) : (
              <>
                <p>Generate</p>
                <ArrowPathIcon className='h-[20px] w-[20px]' />
              </>
            )}
          </button>
          {userStoryInput !== '' && (
            <button
              className="h-[40px] flex flex-row justify-center items-center space-x-3 bg-[#3b54d0] text-white shadow-md rounded-[16px] mt-[28px] p-2"
              onClick={onClearPress}
              disabled={isLoading}
            >
              Clear
            </button>
          )}
        </div>
      </div>
      <div className="flex flex-1 flex-col items-center">
        <div
          className="min-h-[350px] max-h-[500px] flex flex-1 flex-col bg-gray-800 rounded-[24px] w-full
          p-[20px] shadow-md text-gray-200 border-[1px] space-y-[16px] border-gray-600 overflow-scroll no-scrollbar">
          {testCases && (
            testCases.results.map((testCase, testCaseIndex) => (
              <div className='' key={testCaseIndex}>
                <h3 className='text-[18px] font-bold'>{testCase.test}</h3>
                <h4 className='text-[16px] font-medium'>Expects:</h4>
                <ul className='ml-[20px]'>
                  {testCase.expects.map((expect, expectIndex) => (
                    <li className='text-gray-400' key={expectIndex}>- {expect}</li>
                  ))}
                </ul>
                <h4 className='text-[16px] font-medium'>Steps:</h4>
                <ul className='ml-[20px]'>
                  {testCase.steps.map((step, stepIndex) => (
                    <li className='text-gray-400' key={stepIndex}>- {step}</li>
                  ))}
                </ul>
                <div className='w-full h-[1px] bg-gray-500 mt-[8px]' />
              </div>
            ))
          )}
        </div>
        {csv && (
          <a
            className="w-[197px] h-[40px] flex flex-row justify-center items-center space-x-3 bg-[#3b54d0] text-white shadow-md rounded-[16px] mt-[28px] p-2"
            target="_self"
            id='excel-file'
          >
            <p>Save to Excel</p>
            <img src="/csv.svg" alt='csv'/>
          </a>
        )}
        {!csv && <div className="w-[197px] h-[40px] mt-[28px] p-2" />}
      </div>
    </div>
  );
};

export default Generation;