import Generation from '@/components/Generation'
import Instructions from '@/components/Instructions'
import SearchBar from '@/components/SearchBar'

export default function Home() {
  return (
    <main className="flex flex-1 flex-col h-full mt-[37px]">
      {/* <SearchBar /> */}
      <Generation />
      <Instructions />
    </main>
  )
}
