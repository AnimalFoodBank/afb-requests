

/**
 * Generates an array of strings representing a range of years from a
 * specified floor year up to the current year. If no floor year is
 * provided, defaults to 1980.
 *
 * @param floorYear The starting year of the range (default: 1980)
 * @returns An array of strings representing the range of years
 */
const generateYearRange = (floorYear: number = 1980): string[] => {
  const currentYear = new Date().getFullYear();
  const yearRange = currentYear - floorYear + 1;

  return Array.from(
    { length: yearRange },
    (_, i) => String(currentYear - i)
  );
};

export { generateYearRange };
