// ES6 class keyword

class SimpleDate {
  constructor(year, month, day) {
    // Check that (year, month, day) is a valid date
    // ...

    // If it is, use it to initialize "this" date
    this._year = year;
    this._month = month;
    this._day = day;
  }

  getDay() {
    return this._day;
  }
}

date = new SimpleDate(2017, 12, 09);
console.log(date.getDay());
console.log(date._year)

