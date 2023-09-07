/**
 * @classdesc Foo is super important for this sphinx project
 */
class Foo {
  /**
   * Create a Foo instance.
   * @constructor
   * @param {number} value - The initial value for member.
   */
  constructor(value) {
    /**
     * @private
     * @type {number}
     */
    this.member = value;
  }

  /**
   * Perform some work using the private member.
   * @public
   * @param {number} bar - this parameter is mandatory.
   * @returns {number} The work results
   */
  doSomeWork(bar) {
    // Perform some work using this.member
    const result = `Work done with '${this.member}' using parameter '${workParam}'.`;
    return result;
  }
}