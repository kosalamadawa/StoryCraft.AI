'use client'

import { getPrediction } from '@/service/api';
import { ArrowPathIcon } from '@heroicons/react/24/outline';
import BeatLoader from "react-spinners/BeatLoader";
import { useState } from 'react';

const Generation: React.FC = () => {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [userStoryInput, setUserStoryInput] = useState<string>('');
  const [testCases, setTestCases] = useState<APIResponse>();

  const onGeneratePress = async (event: any) => {
    event.preventDefault();
    if (userStoryInput !== '') {
      try {
        setIsLoading(true);
        const response = await getPrediction(userStoryInput);
        setTestCases(response);
        setIsLoading(false);
      } catch (error) {
        console.error(error);
      }
    };
  };

  return (
    <div className="flex flex-1 flex-row justify-between space-x-[20px]">
      <div className="flex flex-1 flex-col items-center">
        <div className="min-h-[350px] h-full w-full bg-gray-800 rounded-[24px] shadow-md border-[1px] border-gray-600">
          <textarea
            className="bg-gray-800 h-full w-full ring-0 outline-0 p-4 rounded-[24px] text-gray-200"
            placeholder="Write the acceptance criteria"
            onChange={(event) => setUserStoryInput(event.target.value)}
          />
        </div>
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
      </div>
      <div className="flex flex-1 flex-col items-center">
        <div
          className="min-h-[350px] max-h-[500px] flex flex-1 flex-col bg-gray-800 rounded-[24px] w-full
          p-[20px] shadow-md text-gray-200 border-[1px] space-y-[16px] border-gray-600 overflow-scroll no-scrollbar">
          {testCases && (
            testCases.results.map((testCase) => (
              <div className=''>
                <h3 className='text-[18px] font-bold'>{testCase.test}</h3>
                <h4 className='text-[16px] font-medium'>Expects:</h4>
                <ul className='ml-[20px]'>
                  {testCase.expects.map(expect => (
                    <li className='text-gray-400'>- {expect}</li>
                  ))}
                </ul>
                <h4 className='text-[16px] font-medium'>Steps:</h4>
                <ul className='ml-[20px]'>
                  {testCase.steps.map(step => (
                    <li className='text-gray-400'>- {step}</li>
                  ))}
                </ul>
                <div className='w-full h-[1px] bg-gray-500 mt-[8px]' />
              </div>
            ))
          )}
        </div>
        <button
          className="w-[197px] h-[40px] flex flex-row justify-center items-center space-x-3 bg-[#3b54d0] text-white shadow-md rounded-[16px] mt-[28px] p-2"
        >
          <p>Save to Excel</p>
          <img src="/csv.svg"/>
        </button>
      </div>
    </div>
  );
};

export default Generation;