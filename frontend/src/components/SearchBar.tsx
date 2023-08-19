'use client'

import { MagnifyingGlassIcon } from '@heroicons/react/24/outline';

const SearchBar: React.FC = () => {
  return (
    <div className="w-full flex flex-row items-center bg-[#F6F6FB] rounded-[4px] space-x-[8px] p-2 shadow-md">
      <MagnifyingGlassIcon className="h-[18px] w-[18px] text-[#AAA8AF]" />
      <input
        className='flex-1 bg-[#F6F6FB] ring-0 outline-0'
        placeholder='Search'
      />
    </div>
  );
};

export default SearchBar;