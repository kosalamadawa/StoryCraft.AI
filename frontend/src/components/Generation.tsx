import { ArrowPathIcon } from '@heroicons/react/24/outline';

const Generation: React.FC = () => {
  return (
    <div className="flex flex-1 flex-row justify-between space-x-[20px]">
      <div className="flex flex-1 flex-col items-center">
        <div className="min-h-[350px] h-full w-full bg-gray-800 rounded-[24px] shadow-md border-[1px] border-gray-600">
          <textarea
            className="bg-gray-800 h-full w-full ring-0 outline-0 p-4 rounded-[24px] text-gray-200"
            placeholder="Write the acceptance criteria"
          />
        </div>
        <button
          className="w-[197px] h-[40px] flex flex-row justify-center items-center space-x-3 bg-[#3b54d0] text-white shadow-md rounded-[16px] mt-[28px] p-2"
        >
          <p>Generate</p>
          <ArrowPathIcon className='h-[20px] w-[20px]' />
        </button>
      </div>
      <div className="flex flex-1 flex-col items-center">
        <div className="min-h-[350px] flex flex-1 bg-gray-800 rounded-[24px] p-4 shadow-md text-gray-200 border-[1px] border-gray-600">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit tempora dignissimos fugiat,
          sequi tempore aut quo molestiae aperiam doloribus ipsa ab cumque quos. Doloribus corrupti hic
          maiores commodi voluptatum autem.
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