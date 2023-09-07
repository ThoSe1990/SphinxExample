#pragma once 


/**
 *  foo is super important for this sphinx project
 */
class foo
{
  public:
    /**
    * This does some work 
    * @param bar this parameter is mandatory.
    * @return The work results
    */
    int do_some_work(int bar);
  
  private:

    /** 
    * a private member.
    * which we can not ignore
    */
    std::size_t m_member;
};